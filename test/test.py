from locust import task, run_single_user
from locust import FastHttpUser


class wbw_1(FastHttpUser):
    host = "https://wbw.one"
    default_headers = {
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    @task
    def t(self):
        with self.client.request(
            "POST",
            "/results.json",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1684",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": "P5=eyJpdiI6IjhkcDBHUk8zV2M1QTlEV1Z0clc4QWc9PSIsInZhbHVlIjoiaklOTW9oSm9Idk12czZCZGJOdVpBUT09IiwibWFjIjoiMGU5ZjgyOTAzMTc0Y2E5OWYyZmY3NmIzZTMxMmE5NmFkMDdmMzc0MDMyYTM0ODVkZjdmODlmOTc2Zjg2ZjliOSJ9; P9=eyJpdiI6InMrUnlSam9vZTRjMmFPYmFwa0RmWWc9PSIsInZhbHVlIjoiMG5FZkVjYW9VanM1MFE5SnZXWXBlZz09IiwibWFjIjoiOTE2YTEwNmIxZTMwM2E4ZTU1OTBmMzQ3MDhlY2ZlOTg3YzIwZGVhYzUxMTdkZGRhODIzYmUzYzI4MmExYWMyMiJ9; P6=eyJpdiI6Ilh1OGFkSjh3VzJ2aklqTzJnclwvTE53PT0iLCJ2YWx1ZSI6InRjWStkemV4V2h3Mnl1U3VBQ3BOWFE9PSIsIm1hYyI6IjgyNDUzNGJkMzk5NDJhMDZmZDBiY2FlYmZhZGQ5NzA3NjU0YTM2YTgzYjIzOTRmOWQ2NjdjYTE5YjE3YjExZmEifQ%3D%3D; P3=eyJpdiI6Ik8wbmViRFE4VWtXSXlMUlwvY0ZPcTl3PT0iLCJ2YWx1ZSI6IjFrUFZUS0dENUhHOUVjREpmbTFtUXc9PSIsIm1hYyI6ImExMjIxODdkN2NjNTc4Y2NhYzlmZDUyMjEzZTQ4MjMzNTI4NzJlNmU1YjZjYWMyMTJhNDM2MTMyNjU4N2M0NGIifQ%3D%3D; P2=eyJpdiI6IjdZeFg0RU16Z1NVYWEyT1FuU0ppbEE9PSIsInZhbHVlIjoiNjZaSFk5XC9KbWt1TTJoM1ZIb1VwUmc9PSIsIm1hYyI6ImFlNmJjYjNmOTQzN2ZlNTQxZDkwYjk1YWFhZjVkNjViYjUxOGI3ZGU4NWFmMmI0NDk0MmQ2YjkyNDIwN2U5ZWQifQ%3D%3D; P1=eyJpdiI6IjFZcDFteFVBc3F4ZjBwS0hOTVlJUVE9PSIsInZhbHVlIjoiSytBaXNOYUZ4Q3dwdGhaaVwvM0JTS2c9PSIsIm1hYyI6IjkyNDUwODVlOTlkYTU0MmU3MGM4MjNkMjhhMGE5MjAwMDI0NTQ5MjBmM2ExMjM5OGI0YmY1Yjc3MDEyM2RmMDAifQ%3D%3D; _hjid=8433baee-ca97-4141-8a5d-d1a00053e8cd; _hjSessionUser_1265371=eyJpZCI6IjE5MmVlNzAzLTM0YjctNWYyYS1hMDc5LTg2YTljNjhkNzc3ZSIsImNyZWF0ZWQiOjE2ODkzNTExNjk0MDMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1551374200.1691179681; XSRF-TOKEN=eyJpdiI6IjhFbFpzM2JtWjRaWHl4bktYNEZyYkE9PSIsInZhbHVlIjoiRVZITGt1clpOTjQwbGk1NFBmUVAxbFVWZjZMSHA1WGo1MENKN3JYZUc3THJEYzVNdGkwc05rK2FtbHdOTDJLWCIsIm1hYyI6IjU1ZGQzNzRiODVmNjA2ZTY3MmFjZWY1MzlmNWM1ZjcxNTc1NjhkMWVhZDJhZmU4NGNjZWRjM2JhODU4YjkwZjgifQ%3D%3D; laravel_session=eyJpdiI6Ik95bHhhNVZuREJcL2I4MXpsRlFaa2tRPT0iLCJ2YWx1ZSI6InVOSmxPSm5VWHY5bFhmaHZ3azFwUDltWGg3MUdQOExGYTZXMzladFU1eUVsMG50NHJKVFRqelg2UFlPVFFxa0siLCJtYWMiOiIzNTE5NDA2YzEyN2UwYTU0MTZhMjg3NjNkMzkyN2ZkZDY0NDQxY2VlNjM5ZjRlNzhmMjY2YTJiZTQ4OThmNTc5In0%3D; _ga_8RW9HZ1T6G=GS1.1.1691264634.30.1.1691264634.0.0.0; _ga=GA1.2.527940208.1687686403; _gat_gtag_UA_124348278_2=1",
                "Host": "wbw.one",
                "Origin": "https://wbw.one",
                "Referer": "https://wbw.one/trusttrail/1",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data="questions%5B0%5D%5Brt%5D=1238&questions%5B0%5D%5Bstimulus%5D=Deze+vraag+gaat+over+je+vertrouwen+in+de+mini-samenleving+die+Lowlands+momenteel+vormt.+Is+je+zelfvertrouwen+sinds+je+op+dit+muziekfestival+bent+toegenomen+of+afgenomen%3F&questions%5B0%5D%5Bbutton_pressed%5D=0&questions%5B0%5D%5Border%5D=2&questions%5B0%5D%5Bquestion_id%5D=6409&questions%5B0%5D%5Bexperiment_id%5D=540&questions%5B0%5D%5Bmodule_id%5D=2238&questions%5B0%5D%5Btrial_type%5D=button-response&questions%5B0%5D%5Btrial_index%5D=2&questions%5B0%5D%5Btime_elapsed%5D=23949&questions%5B0%5D%5Binternal_node_id%5D=0.0-2.0&questions%5B1%5D%5Brt%5D=1167&questions%5B1%5D%5Bstimulus%5D=Hoeveel+geld+zou+je+uitlenen%3F&questions%5B1%5D%5Bbutton_pressed%5D=0&questions%5B1%5D%5Border%5D=3&questions%5B1%5D%5Bquestion_id%5D=6410&questions%5B1%5D%5Bexperiment_id%5D=540&questions%5B1%5D%5Bmodule_id%5D=2240&questions%5B1%5D%5Btrial_type%5D=button-response&questions%5B1%5D%5Btrial_index%5D=3&questions%5B1%5D%5Btime_elapsed%5D=25220&questions%5B1%5D%5Binternal_node_id%5D=0.0-3.0&questions%5B2%5D%5Brt%5D=1143&questions%5B2%5D%5Bstimulus%5D=Is+je+vertrouwen+door+wat+er+momenteel+in+Nederland+en%2Fof+in+de+wereld+gebeurt+toegenomen+of+afgenomen%3F+Deze+vraag+gaat+vooral+over+je+vertrouwen+in+de+maatschappij.&questions%5B2%5D%5Bbutton_pressed%5D=0&questions%5B2%5D%5Border%5D=4&questions%5B2%5D%5Bquestion_id%5D=6411&questions%5B2%5D%5Bexperiment_id%5D=540&questions%5B2%5D%5Bmodule_id%5D=2241&questions%5B2%5D%5Btrial_type%5D=button-response&questions%5B2%5D%5Btrial_index%5D=4&questions%5B2%5D%5Btime_elapsed%5D=26467&questions%5B2%5D%5Binternal_node_id%5D=0.0-4.0&X-CSRF-TOKEN=FXSLi3sPU8QY1jGkwPvZlOt4hTmvFsPlT08B0kIy",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/trusttrail.debrief?result=0",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Cookie": "P5=eyJpdiI6IjhkcDBHUk8zV2M1QTlEV1Z0clc4QWc9PSIsInZhbHVlIjoiaklOTW9oSm9Idk12czZCZGJOdVpBUT09IiwibWFjIjoiMGU5ZjgyOTAzMTc0Y2E5OWYyZmY3NmIzZTMxMmE5NmFkMDdmMzc0MDMyYTM0ODVkZjdmODlmOTc2Zjg2ZjliOSJ9; P9=eyJpdiI6InMrUnlSam9vZTRjMmFPYmFwa0RmWWc9PSIsInZhbHVlIjoiMG5FZkVjYW9VanM1MFE5SnZXWXBlZz09IiwibWFjIjoiOTE2YTEwNmIxZTMwM2E4ZTU1OTBmMzQ3MDhlY2ZlOTg3YzIwZGVhYzUxMTdkZGRhODIzYmUzYzI4MmExYWMyMiJ9; P6=eyJpdiI6Ilh1OGFkSjh3VzJ2aklqTzJnclwvTE53PT0iLCJ2YWx1ZSI6InRjWStkemV4V2h3Mnl1U3VBQ3BOWFE9PSIsIm1hYyI6IjgyNDUzNGJkMzk5NDJhMDZmZDBiY2FlYmZhZGQ5NzA3NjU0YTM2YTgzYjIzOTRmOWQ2NjdjYTE5YjE3YjExZmEifQ%3D%3D; P3=eyJpdiI6Ik8wbmViRFE4VWtXSXlMUlwvY0ZPcTl3PT0iLCJ2YWx1ZSI6IjFrUFZUS0dENUhHOUVjREpmbTFtUXc9PSIsIm1hYyI6ImExMjIxODdkN2NjNTc4Y2NhYzlmZDUyMjEzZTQ4MjMzNTI4NzJlNmU1YjZjYWMyMTJhNDM2MTMyNjU4N2M0NGIifQ%3D%3D; P2=eyJpdiI6IjdZeFg0RU16Z1NVYWEyT1FuU0ppbEE9PSIsInZhbHVlIjoiNjZaSFk5XC9KbWt1TTJoM1ZIb1VwUmc9PSIsIm1hYyI6ImFlNmJjYjNmOTQzN2ZlNTQxZDkwYjk1YWFhZjVkNjViYjUxOGI3ZGU4NWFmMmI0NDk0MmQ2YjkyNDIwN2U5ZWQifQ%3D%3D; P1=eyJpdiI6IjFZcDFteFVBc3F4ZjBwS0hOTVlJUVE9PSIsInZhbHVlIjoiSytBaXNOYUZ4Q3dwdGhaaVwvM0JTS2c9PSIsIm1hYyI6IjkyNDUwODVlOTlkYTU0MmU3MGM4MjNkMjhhMGE5MjAwMDI0NTQ5MjBmM2ExMjM5OGI0YmY1Yjc3MDEyM2RmMDAifQ%3D%3D; _hjid=8433baee-ca97-4141-8a5d-d1a00053e8cd; _hjSessionUser_1265371=eyJpZCI6IjE5MmVlNzAzLTM0YjctNWYyYS1hMDc5LTg2YTljNjhkNzc3ZSIsImNyZWF0ZWQiOjE2ODkzNTExNjk0MDMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1551374200.1691179681; XSRF-TOKEN=eyJpdiI6IjhFbFpzM2JtWjRaWHl4bktYNEZyYkE9PSIsInZhbHVlIjoiRVZITGt1clpOTjQwbGk1NFBmUVAxbFVWZjZMSHA1WGo1MENKN3JYZUc3THJEYzVNdGkwc05rK2FtbHdOTDJLWCIsIm1hYyI6IjU1ZGQzNzRiODVmNjA2ZTY3MmFjZWY1MzlmNWM1ZjcxNTc1NjhkMWVhZDJhZmU4NGNjZWRjM2JhODU4YjkwZjgifQ%3D%3D; laravel_session=eyJpdiI6Ik95bHhhNVZuREJcL2I4MXpsRlFaa2tRPT0iLCJ2YWx1ZSI6InVOSmxPSm5VWHY5bFhmaHZ3azFwUDltWGg3MUdQOExGYTZXMzladFU1eUVsMG50NHJKVFRqelg2UFlPVFFxa0siLCJtYWMiOiIzNTE5NDA2YzEyN2UwYTU0MTZhMjg3NjNkMzkyN2ZkZDY0NDQxY2VlNjM5ZjRlNzhmMjY2YTJiZTQ4OThmNTc5In0%3D; _ga_8RW9HZ1T6G=GS1.1.1691264634.30.1.1691264634.0.0.0; _ga=GA1.2.527940208.1687686403; _gat_gtag_UA_124348278_2=1",
                "Host": "wbw.one",
                "Referer": "https://wbw.one/trusttrail/1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/trusttrail/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Cookie": "P5=eyJpdiI6IjhkcDBHUk8zV2M1QTlEV1Z0clc4QWc9PSIsInZhbHVlIjoiaklOTW9oSm9Idk12czZCZGJOdVpBUT09IiwibWFjIjoiMGU5ZjgyOTAzMTc0Y2E5OWYyZmY3NmIzZTMxMmE5NmFkMDdmMzc0MDMyYTM0ODVkZjdmODlmOTc2Zjg2ZjliOSJ9; P9=eyJpdiI6InMrUnlSam9vZTRjMmFPYmFwa0RmWWc9PSIsInZhbHVlIjoiMG5FZkVjYW9VanM1MFE5SnZXWXBlZz09IiwibWFjIjoiOTE2YTEwNmIxZTMwM2E4ZTU1OTBmMzQ3MDhlY2ZlOTg3YzIwZGVhYzUxMTdkZGRhODIzYmUzYzI4MmExYWMyMiJ9; P6=eyJpdiI6Ilh1OGFkSjh3VzJ2aklqTzJnclwvTE53PT0iLCJ2YWx1ZSI6InRjWStkemV4V2h3Mnl1U3VBQ3BOWFE9PSIsIm1hYyI6IjgyNDUzNGJkMzk5NDJhMDZmZDBiY2FlYmZhZGQ5NzA3NjU0YTM2YTgzYjIzOTRmOWQ2NjdjYTE5YjE3YjExZmEifQ%3D%3D; P3=eyJpdiI6Ik8wbmViRFE4VWtXSXlMUlwvY0ZPcTl3PT0iLCJ2YWx1ZSI6IjFrUFZUS0dENUhHOUVjREpmbTFtUXc9PSIsIm1hYyI6ImExMjIxODdkN2NjNTc4Y2NhYzlmZDUyMjEzZTQ4MjMzNTI4NzJlNmU1YjZjYWMyMTJhNDM2MTMyNjU4N2M0NGIifQ%3D%3D; P2=eyJpdiI6IjdZeFg0RU16Z1NVYWEyT1FuU0ppbEE9PSIsInZhbHVlIjoiNjZaSFk5XC9KbWt1TTJoM1ZIb1VwUmc9PSIsIm1hYyI6ImFlNmJjYjNmOTQzN2ZlNTQxZDkwYjk1YWFhZjVkNjViYjUxOGI3ZGU4NWFmMmI0NDk0MmQ2YjkyNDIwN2U5ZWQifQ%3D%3D; P1=eyJpdiI6IjFZcDFteFVBc3F4ZjBwS0hOTVlJUVE9PSIsInZhbHVlIjoiSytBaXNOYUZ4Q3dwdGhaaVwvM0JTS2c9PSIsIm1hYyI6IjkyNDUwODVlOTlkYTU0MmU3MGM4MjNkMjhhMGE5MjAwMDI0NTQ5MjBmM2ExMjM5OGI0YmY1Yjc3MDEyM2RmMDAifQ%3D%3D; _hjid=8433baee-ca97-4141-8a5d-d1a00053e8cd; _hjSessionUser_1265371=eyJpZCI6IjE5MmVlNzAzLTM0YjctNWYyYS1hMDc5LTg2YTljNjhkNzc3ZSIsImNyZWF0ZWQiOjE2ODkzNTExNjk0MDMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1551374200.1691179681; _gat_gtag_UA_124348278_2=1; XSRF-TOKEN=eyJpdiI6IlVSeUFoc295cThqXC96MTNqU3hXS2lRPT0iLCJ2YWx1ZSI6Ik1TbGVIaFwvWFZxWXdrQXpjWkZVSytmSFFTNnVDS0VKanBEUTc3NkJSbWJLXC9NK0N2K09tRGdQKzE1eitNd1wvWHgiLCJtYWMiOiI3YzM5ZWQ3ODI3NjUzY2UwYWU3YzkzYzE0MjM1OGY5NDdiYTU3Y2MzYTFlMjIxY2Y0MjQxODc0ZWU4OWIyMmEwIn0%3D; laravel_session=eyJpdiI6InUyNXBHMkdteTZRNHdLeGtManVYXC9RPT0iLCJ2YWx1ZSI6Im1Gdk8zWEtCbDZ2dThrMTl3dFNYQ2tsWmhueDhmU0N0VE81ckZQRGd6UnEzMW1NWXROVExNekYyUSt4eEVnTGkiLCJtYWMiOiIzMjdjN2ZhMmJmOTBjNjI5N2RhY2QzY2U2M2I4ZjM1ZWViZDk0OWIxM2I2NDYzMDgzYmM4ZDlmZTkwZDA4OGM2In0%3D; _ga_8RW9HZ1T6G=GS1.1.1691264634.30.1.1691264661.0.0.0; _ga=GA1.2.527940208.1687686403",
                "Host": "wbw.one",
                "Referer": "https://wbw.one/trusttrail.debrief?result=0",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/trusttrail/1",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Cookie": "P5=eyJpdiI6IjhkcDBHUk8zV2M1QTlEV1Z0clc4QWc9PSIsInZhbHVlIjoiaklOTW9oSm9Idk12czZCZGJOdVpBUT09IiwibWFjIjoiMGU5ZjgyOTAzMTc0Y2E5OWYyZmY3NmIzZTMxMmE5NmFkMDdmMzc0MDMyYTM0ODVkZjdmODlmOTc2Zjg2ZjliOSJ9; P9=eyJpdiI6InMrUnlSam9vZTRjMmFPYmFwa0RmWWc9PSIsInZhbHVlIjoiMG5FZkVjYW9VanM1MFE5SnZXWXBlZz09IiwibWFjIjoiOTE2YTEwNmIxZTMwM2E4ZTU1OTBmMzQ3MDhlY2ZlOTg3YzIwZGVhYzUxMTdkZGRhODIzYmUzYzI4MmExYWMyMiJ9; P6=eyJpdiI6Ilh1OGFkSjh3VzJ2aklqTzJnclwvTE53PT0iLCJ2YWx1ZSI6InRjWStkemV4V2h3Mnl1U3VBQ3BOWFE9PSIsIm1hYyI6IjgyNDUzNGJkMzk5NDJhMDZmZDBiY2FlYmZhZGQ5NzA3NjU0YTM2YTgzYjIzOTRmOWQ2NjdjYTE5YjE3YjExZmEifQ%3D%3D; P3=eyJpdiI6Ik8wbmViRFE4VWtXSXlMUlwvY0ZPcTl3PT0iLCJ2YWx1ZSI6IjFrUFZUS0dENUhHOUVjREpmbTFtUXc9PSIsIm1hYyI6ImExMjIxODdkN2NjNTc4Y2NhYzlmZDUyMjEzZTQ4MjMzNTI4NzJlNmU1YjZjYWMyMTJhNDM2MTMyNjU4N2M0NGIifQ%3D%3D; P2=eyJpdiI6IjdZeFg0RU16Z1NVYWEyT1FuU0ppbEE9PSIsInZhbHVlIjoiNjZaSFk5XC9KbWt1TTJoM1ZIb1VwUmc9PSIsIm1hYyI6ImFlNmJjYjNmOTQzN2ZlNTQxZDkwYjk1YWFhZjVkNjViYjUxOGI3ZGU4NWFmMmI0NDk0MmQ2YjkyNDIwN2U5ZWQifQ%3D%3D; P1=eyJpdiI6IjFZcDFteFVBc3F4ZjBwS0hOTVlJUVE9PSIsInZhbHVlIjoiSytBaXNOYUZ4Q3dwdGhaaVwvM0JTS2c9PSIsIm1hYyI6IjkyNDUwODVlOTlkYTU0MmU3MGM4MjNkMjhhMGE5MjAwMDI0NTQ5MjBmM2ExMjM5OGI0YmY1Yjc3MDEyM2RmMDAifQ%3D%3D; _hjid=8433baee-ca97-4141-8a5d-d1a00053e8cd; _hjSessionUser_1265371=eyJpZCI6IjE5MmVlNzAzLTM0YjctNWYyYS1hMDc5LTg2YTljNjhkNzc3ZSIsImNyZWF0ZWQiOjE2ODkzNTExNjk0MDMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1551374200.1691179681; _ga=GA1.2.527940208.1687686403; XSRF-TOKEN=eyJpdiI6InZhaUtJYkdHV3VEUWJGZnM3RXk2UGc9PSIsInZhbHVlIjoiaUxpaHNRd3E0cTgyaGJmR0k3aG5aa0tpSHlLSkljWitJTzYwWEZreG5IR3Nob2FhU2x0bjRmQWgzc1JXaWZPViIsIm1hYyI6ImY2MTk5YjQ1OGE2YmIyZDFlYjgzMjQ0MjE1ZTBkZTVhYTRlYWRmYjRlNzZiYmYxMTA4NDIwOTM3ZTVkMzIxMGQifQ%3D%3D; laravel_session=eyJpdiI6IlRQcEhldk1YeTV2a0ZlV050amZBTnc9PSIsInZhbHVlIjoiTTUzaUdRSVlcL0FpRlNybExJQjQ3d0w2NjB2cXpwXC9oMFV6OEQ0Y2J2eEtWZmtTUlc3S2NMdTlqM1JTZVlnY1JIIiwibWFjIjoiMTg4NTFmNjZmYzg4MDZjNzYwMTYxYWE5YjUwZGRkM2VjMjExMjIzMjVlZjQ0MWZmYzgyN2E5MzY5ZmVlNjNlNCJ9; _ga_8RW9HZ1T6G=GS1.1.1691264634.30.1.1691265217.0.0.0",
                "Host": "wbw.one",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://www.google-analytics.com/j/collect?v=1&_v=j101&a=178129221&t=pageview&_s=1&dl=https%3A%2F%2Fwbw.one%2Ftrusttrail%2F1&ul=nl-nl&de=UTF-8&dt=WorldBrainWave&sd=24-bit&sr=1280x800&vp=1254x624&je=0&_u=QACAAUABAAAAACAAI~&jid=412495405&gjid=1251648689&cid=527940208.1687686403&tid=UA-124348278-2&_gid=1551374200.1691179681&_r=1&gtm=457e3820&jsscut=1&z=1436181141",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "text/plain",
                "origin": "https://wbw.one",
                "referer": "https://wbw.one/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/results.json",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1682",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": "P5=eyJpdiI6IjhkcDBHUk8zV2M1QTlEV1Z0clc4QWc9PSIsInZhbHVlIjoiaklOTW9oSm9Idk12czZCZGJOdVpBUT09IiwibWFjIjoiMGU5ZjgyOTAzMTc0Y2E5OWYyZmY3NmIzZTMxMmE5NmFkMDdmMzc0MDMyYTM0ODVkZjdmODlmOTc2Zjg2ZjliOSJ9; P9=eyJpdiI6InMrUnlSam9vZTRjMmFPYmFwa0RmWWc9PSIsInZhbHVlIjoiMG5FZkVjYW9VanM1MFE5SnZXWXBlZz09IiwibWFjIjoiOTE2YTEwNmIxZTMwM2E4ZTU1OTBmMzQ3MDhlY2ZlOTg3YzIwZGVhYzUxMTdkZGRhODIzYmUzYzI4MmExYWMyMiJ9; P6=eyJpdiI6Ilh1OGFkSjh3VzJ2aklqTzJnclwvTE53PT0iLCJ2YWx1ZSI6InRjWStkemV4V2h3Mnl1U3VBQ3BOWFE9PSIsIm1hYyI6IjgyNDUzNGJkMzk5NDJhMDZmZDBiY2FlYmZhZGQ5NzA3NjU0YTM2YTgzYjIzOTRmOWQ2NjdjYTE5YjE3YjExZmEifQ%3D%3D; P3=eyJpdiI6Ik8wbmViRFE4VWtXSXlMUlwvY0ZPcTl3PT0iLCJ2YWx1ZSI6IjFrUFZUS0dENUhHOUVjREpmbTFtUXc9PSIsIm1hYyI6ImExMjIxODdkN2NjNTc4Y2NhYzlmZDUyMjEzZTQ4MjMzNTI4NzJlNmU1YjZjYWMyMTJhNDM2MTMyNjU4N2M0NGIifQ%3D%3D; P2=eyJpdiI6IjdZeFg0RU16Z1NVYWEyT1FuU0ppbEE9PSIsInZhbHVlIjoiNjZaSFk5XC9KbWt1TTJoM1ZIb1VwUmc9PSIsIm1hYyI6ImFlNmJjYjNmOTQzN2ZlNTQxZDkwYjk1YWFhZjVkNjViYjUxOGI3ZGU4NWFmMmI0NDk0MmQ2YjkyNDIwN2U5ZWQifQ%3D%3D; P1=eyJpdiI6IjFZcDFteFVBc3F4ZjBwS0hOTVlJUVE9PSIsInZhbHVlIjoiSytBaXNOYUZ4Q3dwdGhaaVwvM0JTS2c9PSIsIm1hYyI6IjkyNDUwODVlOTlkYTU0MmU3MGM4MjNkMjhhMGE5MjAwMDI0NTQ5MjBmM2ExMjM5OGI0YmY1Yjc3MDEyM2RmMDAifQ%3D%3D; _hjid=8433baee-ca97-4141-8a5d-d1a00053e8cd; _hjSessionUser_1265371=eyJpZCI6IjE5MmVlNzAzLTM0YjctNWYyYS1hMDc5LTg2YTljNjhkNzc3ZSIsImNyZWF0ZWQiOjE2ODkzNTExNjk0MDMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1551374200.1691179681; XSRF-TOKEN=eyJpdiI6IkVMcFwvVlwvcHRoOGdlbkFzQXhiTzJYUT09IiwidmFsdWUiOiJIS21qZWtReitRUEVFWFVlOUNvblpBZkUxTlRrUUlVbTNJeEtmZ3BTcDQ5blBJc1JKcXJSYlA0XC8zZEdHcXV3eSIsIm1hYyI6IjBmZjY5NjU1OTMzYjg0M2IzNjE5ZWUzNTg4NGUzNzk3Zjg0NzE1ZDBkNWY4NWQwZmJhODY5ZWQ4Yjk3YjRiYzIifQ%3D%3D; laravel_session=eyJpdiI6ImIwMkY4YUdCQ1RHRHEzcm50aEJwT2c9PSIsInZhbHVlIjoiZml0NEppXC9VeGk5b0h1ZEw1MW1iZDFYYlBFZWdWMFwvOEpwZDRHV0s4MEJUYmp4TldcL1hlckoxcW1oUWt5Y1dYTyIsIm1hYyI6IjExOWEwNTRlNDYwMWU5YTZkZmEwOWRlNDQ4YmVkMDhlZDg0ZGM0ZmE2MWZmNzhhYWJhNDhjOGMwOTVlY2NmYzcifQ%3D%3D; _gat_gtag_UA_124348278_2=1; _ga_8RW9HZ1T6G=GS1.1.1691264634.30.1.1691265222.0.0.0; _ga=GA1.1.527940208.1687686403",
                "Host": "wbw.one",
                "Origin": "https://wbw.one",
                "Referer": "https://wbw.one/trusttrail/1",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data="questions%5B0%5D%5Brt%5D=2527&questions%5B0%5D%5Bstimulus%5D=Deze+vraag+gaat+over+je+vertrouwen+in+de+mini-samenleving+die+Lowlands+momenteel+vormt.+Is+je+zelfvertrouwen+sinds+je+op+dit+muziekfestival+bent+toegenomen+of+afgenomen%3F&questions%5B0%5D%5Bbutton_pressed%5D=0&questions%5B0%5D%5Border%5D=2&questions%5B0%5D%5Bquestion_id%5D=6409&questions%5B0%5D%5Bexperiment_id%5D=540&questions%5B0%5D%5Bmodule_id%5D=2238&questions%5B0%5D%5Btrial_type%5D=button-response&questions%5B0%5D%5Btrial_index%5D=2&questions%5B0%5D%5Btime_elapsed%5D=6644&questions%5B0%5D%5Binternal_node_id%5D=0.0-2.0&questions%5B1%5D%5Brt%5D=5925&questions%5B1%5D%5Bstimulus%5D=Hoeveel+geld+zou+je+uitlenen%3F&questions%5B1%5D%5Bbutton_pressed%5D=0&questions%5B1%5D%5Border%5D=3&questions%5B1%5D%5Bquestion_id%5D=6410&questions%5B1%5D%5Bexperiment_id%5D=540&questions%5B1%5D%5Bmodule_id%5D=2240&questions%5B1%5D%5Btrial_type%5D=button-response&questions%5B1%5D%5Btrial_index%5D=3&questions%5B1%5D%5Btime_elapsed%5D=12672&questions%5B1%5D%5Binternal_node_id%5D=0.0-3.0&questions%5B2%5D%5Brt%5D=822&questions%5B2%5D%5Bstimulus%5D=Is+je+vertrouwen+door+wat+er+momenteel+in+Nederland+en%2Fof+in+de+wereld+gebeurt+toegenomen+of+afgenomen%3F+Deze+vraag+gaat+vooral+over+je+vertrouwen+in+de+maatschappij.&questions%5B2%5D%5Bbutton_pressed%5D=0&questions%5B2%5D%5Border%5D=4&questions%5B2%5D%5Bquestion_id%5D=6411&questions%5B2%5D%5Bexperiment_id%5D=540&questions%5B2%5D%5Bmodule_id%5D=2241&questions%5B2%5D%5Btrial_type%5D=button-response&questions%5B2%5D%5Btrial_index%5D=4&questions%5B2%5D%5Btime_elapsed%5D=13601&questions%5B2%5D%5Binternal_node_id%5D=0.0-4.0&X-CSRF-TOKEN=FXSLi3sPU8QY1jGkwPvZlOt4hTmvFsPlT08B0kIy",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/trusttrail.debrief?result=0",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Cookie": "P5=eyJpdiI6IjhkcDBHUk8zV2M1QTlEV1Z0clc4QWc9PSIsInZhbHVlIjoiaklOTW9oSm9Idk12czZCZGJOdVpBUT09IiwibWFjIjoiMGU5ZjgyOTAzMTc0Y2E5OWYyZmY3NmIzZTMxMmE5NmFkMDdmMzc0MDMyYTM0ODVkZjdmODlmOTc2Zjg2ZjliOSJ9; P9=eyJpdiI6InMrUnlSam9vZTRjMmFPYmFwa0RmWWc9PSIsInZhbHVlIjoiMG5FZkVjYW9VanM1MFE5SnZXWXBlZz09IiwibWFjIjoiOTE2YTEwNmIxZTMwM2E4ZTU1OTBmMzQ3MDhlY2ZlOTg3YzIwZGVhYzUxMTdkZGRhODIzYmUzYzI4MmExYWMyMiJ9; P6=eyJpdiI6Ilh1OGFkSjh3VzJ2aklqTzJnclwvTE53PT0iLCJ2YWx1ZSI6InRjWStkemV4V2h3Mnl1U3VBQ3BOWFE9PSIsIm1hYyI6IjgyNDUzNGJkMzk5NDJhMDZmZDBiY2FlYmZhZGQ5NzA3NjU0YTM2YTgzYjIzOTRmOWQ2NjdjYTE5YjE3YjExZmEifQ%3D%3D; P3=eyJpdiI6Ik8wbmViRFE4VWtXSXlMUlwvY0ZPcTl3PT0iLCJ2YWx1ZSI6IjFrUFZUS0dENUhHOUVjREpmbTFtUXc9PSIsIm1hYyI6ImExMjIxODdkN2NjNTc4Y2NhYzlmZDUyMjEzZTQ4MjMzNTI4NzJlNmU1YjZjYWMyMTJhNDM2MTMyNjU4N2M0NGIifQ%3D%3D; P2=eyJpdiI6IjdZeFg0RU16Z1NVYWEyT1FuU0ppbEE9PSIsInZhbHVlIjoiNjZaSFk5XC9KbWt1TTJoM1ZIb1VwUmc9PSIsIm1hYyI6ImFlNmJjYjNmOTQzN2ZlNTQxZDkwYjk1YWFhZjVkNjViYjUxOGI3ZGU4NWFmMmI0NDk0MmQ2YjkyNDIwN2U5ZWQifQ%3D%3D; P1=eyJpdiI6IjFZcDFteFVBc3F4ZjBwS0hOTVlJUVE9PSIsInZhbHVlIjoiSytBaXNOYUZ4Q3dwdGhaaVwvM0JTS2c9PSIsIm1hYyI6IjkyNDUwODVlOTlkYTU0MmU3MGM4MjNkMjhhMGE5MjAwMDI0NTQ5MjBmM2ExMjM5OGI0YmY1Yjc3MDEyM2RmMDAifQ%3D%3D; _hjid=8433baee-ca97-4141-8a5d-d1a00053e8cd; _hjSessionUser_1265371=eyJpZCI6IjE5MmVlNzAzLTM0YjctNWYyYS1hMDc5LTg2YTljNjhkNzc3ZSIsImNyZWF0ZWQiOjE2ODkzNTExNjk0MDMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1551374200.1691179681; XSRF-TOKEN=eyJpdiI6IkVMcFwvVlwvcHRoOGdlbkFzQXhiTzJYUT09IiwidmFsdWUiOiJIS21qZWtReitRUEVFWFVlOUNvblpBZkUxTlRrUUlVbTNJeEtmZ3BTcDQ5blBJc1JKcXJSYlA0XC8zZEdHcXV3eSIsIm1hYyI6IjBmZjY5NjU1OTMzYjg0M2IzNjE5ZWUzNTg4NGUzNzk3Zjg0NzE1ZDBkNWY4NWQwZmJhODY5ZWQ4Yjk3YjRiYzIifQ%3D%3D; laravel_session=eyJpdiI6ImIwMkY4YUdCQ1RHRHEzcm50aEJwT2c9PSIsInZhbHVlIjoiZml0NEppXC9VeGk5b0h1ZEw1MW1iZDFYYlBFZWdWMFwvOEpwZDRHV0s4MEJUYmp4TldcL1hlckoxcW1oUWt5Y1dYTyIsIm1hYyI6IjExOWEwNTRlNDYwMWU5YTZkZmEwOWRlNDQ4YmVkMDhlZDg0ZGM0ZmE2MWZmNzhhYWJhNDhjOGMwOTVlY2NmYzcifQ%3D%3D; _gat_gtag_UA_124348278_2=1; _ga_8RW9HZ1T6G=GS1.1.1691264634.30.1.1691265222.0.0.0; _ga=GA1.1.527940208.1687686403",
                "Host": "wbw.one",
                "Referer": "https://wbw.one/trusttrail/1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(wbw_1)
