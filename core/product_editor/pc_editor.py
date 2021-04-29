import settings


def edit_pc(product):
    # 如果没有skuImage则用主图
    describe_imageList = product.skuImageList if product.skuImageList else product.main_images

    # 要插入图片的
    img_tag = """<img src="" style="box-sizing: border-box; padding: 0px; margin: 0px; border-style: none; 
    vertical-align: middle; max-width: 100%;" /> """

    # pc端描述模板 read_lines
    pc_describes = settings.CURRENT_CONFIG.PC_DESCRIBE_TMPL
    read_lines = pc_describes.splitlines()

    # 依次插入到html中
    for image_url in describe_imageList:
        complete_string = img_tag[:10] + image_url + img_tag[10:]

        # 插入到详情列表里
        read_lines.insert(27, complete_string)
        read_lines.insert(27, "\n")

    pc_describes = "".join(read_lines)

    # print(pc_describes)
    # 保存
    product.form_data['detail'] = pc_describes


if __name__ == '__main__':
    pass
