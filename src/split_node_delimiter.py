from textnode import text_type_bold,text_type_code,text_type_image, text_type_italic, text_type_link, text_type_text, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newList = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            newList.append(node)
        else:
            if delimiter not in node.text:
                raise ValueError(f"Delimiter f{delimiter} was not found in text f{node.text}")
            else:
                words = node.text.split(delimiter)
                for i in range(len(words)):
                    if words[i] == "":
                        continue
                    if i % 2 != 0:
                        newList.append(TextNode(words[i], text_type, node.url))
                    else:
                        newList.append(TextNode(words[i], text_type_text, node.url))
    

    return newList

    
        