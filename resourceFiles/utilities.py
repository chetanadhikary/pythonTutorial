import sqlite3 as sqlite


def sql_select_cmd(tbl_name):
    with sqlite.connect("resourceDB.sqlite") as conn:
        cur = conn.cursor()
        response = cur.execute(f"SELECT * FROM {tbl_name}")
        return response.fetchall(),response.description


if __name__=="__main__":
    lst_emp,desc =sql_select_cmd("Employee")
    for desc_i in desc:
        print(desc_i[0])

