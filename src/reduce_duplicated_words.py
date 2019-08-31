#!/usr/bin/env python3

import sqlite3

cn = sqlite3.connect("gts.sqlite3.db")
cn.row_factory = sqlite3.Row

for i in cn.execute("select madde_id, madde from madde"):
    madde_id = i["madde_id"]
    madde = i["madde"]
    for d in cn.execute("select madde_id, madde from madde where madde=?", (madde,)):
        cn.execute("update anlam set madde_id=? where madde_id=?", (madde_id, d["madde_id"]))

cn.commit()