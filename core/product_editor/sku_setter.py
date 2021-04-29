import copy
import json

from icecream import ic

import settings
from core.item import ProductItem


class SkuSetter(object, ):
    """
        请求并替换模板
        1,请求获取页面 2,抽取3，替换
    """

    # 模板sku
    sku_template_json = settings.CURRENT_CONFIG.sku_template

    def __init__(self):
        self.json_list = None  # 最终拼装好的json列表

        self._variant_info = None  # 元组列表

        # DefinitionName 自定义名称取代 “黑色” “白色”
        self.propertyValueDefinitionName = ["style A", "style B", "style C", "style D", "style E", "style F", "style G",
                                            "style H",
                                            "style I", "style J", "style K", "style L", "style M", "style N", ]
        self.propertyValueId_color = [771, 175, 173, 496, 350686, 1052, 29, 691, 10, 350852, 366, 193]
        self.attrVal = ["米黄色", "绿色", "蓝色", "紫色", "棕色", "粉色", "白色", "灰色", "红色", "橙色", "黄色", "黑色", ]

    def __call__(self, *args, **kwargs):
        """
        执行sku编辑任务
        :param args:
        :param kwargs:
        :return:
        """
        product = kwargs["product"]

        # skuImageList = product.l
        self.edit(product=product)

    def variant_info(self, skuImageList):

        """
            通过zip函数将skuImage列表和style X 等变更属性打包成一个元组列表分别修改
        """
        self._variant_info = list(zip(
            skuImageList,
            self.propertyValueDefinitionName,
            self.propertyValueId_color,
            self.attrVal
        ))

        return self._variant_info

    def edit(self, product):
        """
        组装一个新json_list 传给form_data
        根据skuImageList修改sku - [然后分别设置三个尺寸]
        """

        # 有skuImage图
        if product.skuImageList:
            # 如果有skuImage缩略图就正常用template sku 拼补
            # 根据模板写好的框架进行增删改查 改每个SKU 里面的[skuImage,propertyValueDefinitionName,id,propertyValueId,attrVal]

            # 需要的变种信息
            variant_info = self.variant_info(product.skuImageList)

            # 设置sku详细
            self.set(variant_info_list=variant_info)  # 拼补模板sku里面的细节 [id,skuPrice,propertyValueDefinitionName...]

            # 修改sku的id "id": "200000182:193;5:100014064",
            self.sku_id_splicing()  # # 设置id(不同sku的id字串不同)  ["id": "200000182:193;5:100014064",]

            # 保存到产品的表单中去
            product.form_data["aeopAeProductSKUs"] = json.dumps(self.json_list)
            return

        # 无skuimage
        elif not product.skuImageList:
            # 2.如果没有sku图就放主图
            main_images = product.form_data["imageURLs"].strip("'").split(";")[0]
            tmpl = copy.deepcopy(self.sku_template_json)

            tmpl[0]['aeopSKUProperty'][0]['skuImage'] = main_images
            tmpl[1]['aeopSKUProperty'][0]['skuImage'] = main_images
            tmpl[2]['aeopSKUProperty'][0]['skuImage'] = main_images

            # ic(tmpl)
            # 最后替换提交表单form里的sku项
            product.form_data["aeopAeProductSKUs"] = json.dumps(tmpl)
            # ic("没有skuImage - 单主图sku：", template_sku_json)

            return None

    def set(self, variant_info_list):
        # 拷贝一份sku模板
        tmpl = copy.deepcopy(self.sku_template_json)

        self.json_list = []
        # 清空最终列表 保证无误

        # 根据模板写好的框架进行增删改查 改每个SKU 里面的[skuImage,propertyValueDefinitionName,id,propertyValueId,attrVal]
        # ic(self.zippedList)
        for val_tuple in variant_info_list:
            """
                val_tuple ("https://...",192,"黑色",...)
            """
            # 设置缩略图
            tmpl[0]['aeopSKUProperty'][0]['skuImage'] = val_tuple[0]
            tmpl[1]['aeopSKUProperty'][0]['skuImage'] = val_tuple[0]
            tmpl[2]['aeopSKUProperty'][0]['skuImage'] = val_tuple[0]

            # 设置自定义颜色属性
            tmpl[0]['aeopSKUProperty'][0]['propertyValueDefinitionName'] = val_tuple[1]
            tmpl[1]['aeopSKUProperty'][0]['propertyValueDefinitionName'] = val_tuple[1]
            tmpl[2]['aeopSKUProperty'][0]['propertyValueDefinitionName'] = val_tuple[1]
            # 设置propertyValueId_color
            tmpl[0]['aeopSKUProperty'][0]['propertyValueId'] = val_tuple[2]
            tmpl[1]['aeopSKUProperty'][0]['propertyValueId'] = val_tuple[2]
            tmpl[2]['aeopSKUProperty'][0]['propertyValueId'] = val_tuple[2]

            # 设置attrVal
            tmpl[0]['aeopSKUProperty'][0]['attrVal'] = val_tuple[3]
            tmpl[1]['aeopSKUProperty'][0]['attrVal'] = val_tuple[3]
            tmpl[2]['aeopSKUProperty'][0]['attrVal'] = val_tuple[3]

            # 这里使用深拷贝来防止引用
            self.json_list.extend(copy.deepcopy(tmpl))

    def sku_id_splicing(self, ):
        # 设置id  "id": "200000182:193;5:100014064",
        id_demo = "200000182:193;5:100014064"
        json_list = self.json_list
        for i in json_list:
            color_id = i['aeopSKUProperty'][0]['propertyValueId']
            size_id = i['aeopSKUProperty'][1]['propertyValueId']

            size_id, color_id = list(map(str, [size_id, color_id]))

            sku_id = "200000182:" + color_id + ";5:" + size_id
            # 三个尺寸变种sku的id填充
            i['id'] = sku_id
            i['id'] = sku_id
            i['id'] = sku_id


editSKU = SkuSetter()

if __name__ == '__main__':
    paragraph = """
    <tr data-id="46483711763934184" data-cid="200000241">
							<td style="box-sizing:content-box;border-left:none;vertical-align:top;width:24px;min-width:24px;max-width:24px; padding:0;height: 100%;">
								<label style="width: 100%; height: 100%; padding-top:3px;">
									<input name="productBox" type="checkbox" value="46483711763934184" data-shopid="2451968" datename="showdate" subject="Yellow Canary Finch Bird Watching Home Office Room Camp Decor Decal Wall Art Car Sticker Graphic Waterproof PVC 13cmx12.7cm" deliverytime="0" onclick="showSelCheckboxNum(this)">
								</label>
							</td>
							<td class="w80 minW80 maxW80 v-top">
								<div class="imgDivOut m-right0">
									<div class="findGoods epz_out">
										<img data-original="https://ae01.alicdn.com/kf/Hdc2642db09204b75863bc44d2a01683da/Yellow-Canary-Finch-Bird-Watching-Home-Office-Room-Camp-Decor-Decal-Wall-Art-Car-Sticker-Graphic.jpg" class="imgCss lazy" data-order="https://ae01.alicdn.com/kf/Hdc2642db09204b75863bc44d2a01683da/Yellow-Canary-Finch-Bird-Watching-Home-Office-Room-Camp-Decor-Decal-Wall-Art-Car-Sticker-Graphic.jpg" src="https://ae01.alicdn.com/kf/Hdc2642db09204b75863bc44d2a01683da/Yellow-Canary-Finch-Bird-Watching-Home-Office-Room-Camp-Decor-Decal-Wall-Art-Car-Sticker-Graphic.jpg" style="display: block;">
										<div class="pz_o" style="width: 320px;"><div class="pz_po"><div class="pz_at"><a class="pz_btn fr" href="javascript:"><i class="glyphicon glyphicon-search"></i>找货源</a><a class="pz_btn fr" href="javascript:"><span class="m-right10"><i class="attach-icons md-18">add</i><span style="vertical-align: text-bottom;">添加来源</span></span></a></div><div class="pz_img_o" style="width: 300px; height: 300px;"><img src="" data-src="https://ae01.alicdn.com/kf/Hdc2642db09204b75863bc44d2a01683da/Yellow-Canary-Finch-Bird-Watching-Home-Office-Room-Camp-Decor-Decal-Wall-Art-Car-Sticker-Graphic.jpg"></div></div></div></div>
								</div>
								<p class="m0 f-center"><a target="_blank" href="https://www.aliexpress.com/item/1005002308447959.html">速卖通</a></p>
                    </td>
							<td class="minW170 maxW250 f-left v-top word-break">
								<span class="productHead">Yellow Canary Finch Bird Watching Home Office Room Camp Decor Decal Wall Art Car Sticker Graphic Waterproof PVC 13cmx12.7cm</span><br>
								<span class="limingcentUrlpic">
								&nbsp;</span>
								<div>
									<span id="comment_1_46483711763934184" style="color:"></span><span id="comment_2_46483711763934184" data-color="" style="color:"></span>
									</div>
								<div class="fColor2">「<span class="shopName">康康</span>」</div>
								</td>
							<td style="word-break:break-all;vertical-align: top;text-align:left;min-width: 100px;">
								<span class="productClassify">车贴(Car Stickers)</span><br>
								<span class="fColor2">
								</span>
							</td>
							<td colspan="3" style="padding: 0">
                                    <table class="myj-table-in">
                                        <tbody><tr data-productid="200000182:193">
                                                <td class="maxW110">
                                                    <span class="limingcentUrlpic">Style</span><br>
                                                    <span class="limingcentUrlpic"></span>
                                                    </td>
                                                <td class="maxW110 min-W100-imp">
                                                    <div style="display:inline-block;">
                                                        「零」1.75<br>
                                                        </div>
                                                    <span style="position: absolute;margin: 3px 0 0 5px;">
                                                        </span>
                                                </td>
                                                <td class="w80 minW80 maxW80 relative">
                                                    <span>9999</span>
                                                    </td>
                                            </tr>
                                        </tbody></table>
                                    </td>
							<td style="word-break:break-all;vertical-align: top;text-align:left;max-width: 180px;">
								</td>
							<td class="w110 minW110 maxW110 v-top f-left">
								<p class="m0 fColor2">创建:</p>
									<p class="m0">2021-04-25 15:52</p>
									<p class="m0 fColor2">更新:</p>
									<p class="m0">2021-04-25 15:52</p>
								</td>
							<td class="w70 minW70 maxW70 v-top">
								<a href="smtProduct/edit.htm?id=46483711763934184" target="_blank">编辑</a><br>
										<div class="dropdown mLeft10">
												<a class="dropdown-toggle " href="javascript:" data-toggle="dropdown" type="button">发布<span class="caret"></span></a>
												<ul class="dropdown-menu pull-right" style="min-width:50px;">
													<li><a href="javascript:;" onclick="asyncCheckSmtProduct('46483711763934184')">立即发布</a></li>
													<li><a href="javascript:;" onclick="checkTimingPublish('46483711763934184')">定时发布</a></li>
												</ul>
											</div>
										<div class="dropdown">
									<a href="javascript:" class="dropdown-toggle" data-toggle="dropdown" type="button" onclick="" style="margin-left: 10px;">更多<span class="caret"></span></a>
									<ul class="dropdown-menu pull-right" role="menu" aria-labelledby="" style="min-width:70px;">
										<li role="presentation">
												<a href="javascript:" onclick="Remark.addCommentProduct('46483711763934184','smt');">添加备注</a>
											</li>
										<li role="presentation"><a href="javascript:" onclick="delProduct('46483711763934184','')">删除</a></li>
										</ul>
								</div>
								</td>
						</tr>
    """
    product = ProductItem(html_paragraph=paragraph)
    editSKU(product=product)
