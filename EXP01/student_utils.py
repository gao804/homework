def parse_student(line):
    """把一行 name,score 转为字典；无效记录抛出 ValueError。"""
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError("字段数量必须为 2（姓名,成绩）")
    name, score_text = (field.strip() for field in fields)
    if not name:
        raise ValueError("姓名不能为空")
    try:
        score = int(score_text)
    except ValueError as error:
        raise ValueError("成绩必须是整数") from error
    if not 0 <= score <= 100:
        raise ValueError("成绩必须在 0 到 100 之间")
    return {"name": name, "score": score}
