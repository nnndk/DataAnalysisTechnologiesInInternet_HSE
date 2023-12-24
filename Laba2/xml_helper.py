import lxml.etree as et


def apply_transformation(xml_filename: str, xsl_filename: str, txt_filename: str):
    dom = et.parse(xml_filename)
    xslt = et.parse(xsl_filename)
    transform = et.XSLT(xslt)
    new_dom = transform(dom)

    new_dom_to_file(str(new_dom), txt_filename)


def new_dom_to_file(dom: str, txt_filename: str):
    with open(txt_filename, 'w', encoding='UTF-8') as f:
        f.write(dom)


def get_xpath_result_node(xml_filename: str, req: str) -> tuple:
    tree = et.parse(xml_filename)
    return tree, tree.xpath(req)


def get_xpath_result(xml_filename: str, req: str) -> str:
    tree, res = get_xpath_result_node(xml_filename, req)

    return '\n'.join(map(tree.getelementpath, res)) + '\n'


def get_xpath_result_text(xml_filename: str, req: str, unique: bool = False) -> str:
    tree, res = get_xpath_result_node(xml_filename, req)
    res_text = []

    for i in range(len(res)):
        res_text.append(res[i].text)

    if unique:
        res_text = set(res_text)

    return '\n'.join(res_text) + '\n'
