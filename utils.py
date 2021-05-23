def file_read(file: str) -> dict():
    try:
        with open(file, 'r') as f:
            file_contents = f.readlines()
        f.close()
        file_contents = map(lambda line: line.replace('\n', '<br>'), file_contents)
        res_dct = []
        for file_content in file_contents:
            res_dct.append(file_content)

        return res_dct
    except Exception:

        return 'OOOOps!! Check filename!'
