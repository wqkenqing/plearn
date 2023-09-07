from dominate import document
from dominate.tags import table, tr, td, th, style


def tableCreate(data):
    # 创建文档
    doc = document()

    # 添加CSS样式，用于美化表格
    with doc.head:
        style("""
            table {
                width: 50%;
                border-collapse: collapse;
                margin: 20px;
            }
            th, td {
                padding: 10px;
                text-align: center;
                border: 1px solid black;
            }
            th {
                background-color: #ccc;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            tr:nth-child(odd) {
                background-color: #fff;
            }
        """)

    # 创建表格
    with doc.add(table()):
        # 表头
        with tr():
            th("进展状态")
            th("任务名称")

        # 表格内容
        for task, status in data:
            with tr():
                td(task)
                td(status)

