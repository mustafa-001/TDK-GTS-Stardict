#!/usr/bin/env python3

import sqlite3
import os, io, time

cn = sqlite3.connect("gts.sqlite3.db")
cn.row_factory = sqlite3.Row
cnt = 0
with open("Güncel Türkçe Sözlük - Türk Dil Kurumu 2011.txt", "w") as f:
    for i in cn.execute("select madde_id, madde from madde"):
        k = cn.execute(
            "select anlam, anlam_id from anlam where madde_id=?", (i["madde_id"],))
        f.write(i["madde"]+"\t")
        for l in k:
            ozellik_tamad = ""
            for m in cn.execute("select ozellik_id from anlam_ozellik where anlam_id=?", (l["anlam_id"],)):
                for n in cn.execute("select tam_adi from ozellik where ozellik_id=?", (m["ozellik_id"],)):
                    ozellik_tamad = ozellik_tamad+"("+n["tam_adi"]+") "
            if (ozellik_tamad):
                f.write(ozellik_tamad)
            f.write(l["anlam"]+"\\n\\n")
        f.write("\n")
        cnt = cnt+1
        if cnt % 1000 == 0:
            print(cnt/95000*100)
    f.flush()
