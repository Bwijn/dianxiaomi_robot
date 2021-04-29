from bs4 import BeautifulSoup
from core.item import ProductItem
from core.product_editor import edit_pc

snippet = """
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

soup = BeautifulSoup(snippet,'lxml')
p = ProductItem(soup=soup)
edit_pc(product=p)