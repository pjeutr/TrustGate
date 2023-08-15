from locust import HttpUser, task, events
import random

@events.init_command_line_parser.add_listener
def init_parser(parser):
    parser.add_argument(
        '--customarg',
        default="data1", 
        help="It's working"
    )
# parser.add_argument("--customarg", type=str, env_var="LOCUST_MY_ARGUMENT", default="1234", help="It's working")


# select from_unixtime(FLOOR(UNIX_TIMESTAMP(created_at)/(10*60))*(10*60)) as date,
# (SUM(response=0)*10 + SUM(response=1)*8 + SUM(response=2)*6 + SUM(response=3)*4 + SUM(response=4)*2)/count(*) as total, 
# module_id
# -- select *
# from `results` 
# where `module_id` in (2240, 2238, 2248, 2243, 2245, 2246) 
# -- where `module_id` in (2249, 2250, 2252, 2253, 2256, 2255) 
# -- where `module_id` in (2259, 2258, 2261, 2262, 2264, 2265)  
# and created_at > TIMESTAMP('2023-08-05 15:00:00') AND created_at < TIMESTAMP('2025-08-19 02:00:00')
# group by `module_id`, `date`

myheaders = {'Content-Type': 'application/json', 'Accept': 'application/json'}
myheaders = {
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
            }
# $cog = [2240, 2238, 2248, 2243, 2245, 2246];
# $aff = [2249, 2250, 2252, 2253, 2256, 2255];
# $beh = [2259, 2258, 2261, 2262, 2264, 2265];

data1 ="questions%5B0%5D%5Brt%5D=2527&questions%5B0%5D%5Bstimulus%5D=Deze+vraag+gaat+over+je+vertrouwen+in+de+mini-samenleving+die+Lowlands+momenteel+vormt.+Is+je+zelfvertrouwen+sinds+je+op+dit+muziekfestival+bent+toegenomen+of+afgenomen%3F&questions%5B0%5D%5Bbutton_pressed%5D=0&questions%5B0%5D%5Border%5D=2&questions%5B0%5D%5Bquestion_id%5D=6409&questions%5B0%5D%5Bexperiment_id%5D=540&questions%5B0%5D%5Bmodule_id%5D=2238&questions%5B0%5D%5Btrial_type%5D=button-response&questions%5B0%5D%5Btrial_index%5D=2&questions%5B0%5D%5Btime_elapsed%5D=6644&questions%5B0%5D%5Binternal_node_id%5D=0.0-2.0&questions%5B1%5D%5Brt%5D=5925&questions%5B1%5D%5Bstimulus%5D=Hoeveel+geld+zou+je+uitlenen%3F&questions%5B1%5D%5Bbutton_pressed%5D=0&questions%5B1%5D%5Border%5D=3&questions%5B1%5D%5Bquestion_id%5D=6410&questions%5B1%5D%5Bexperiment_id%5D=540&questions%5B1%5D%5Bmodule_id%5D=2240&questions%5B1%5D%5Btrial_type%5D=button-response&questions%5B1%5D%5Btrial_index%5D=3&questions%5B1%5D%5Btime_elapsed%5D=12672&questions%5B1%5D%5Binternal_node_id%5D=0.0-3.0&questions%5B2%5D%5Brt%5D=822&questions%5B2%5D%5Bstimulus%5D=Is+je+vertrouwen+door+wat+er+momenteel+in+Nederland+en%2Fof+in+de+wereld+gebeurt+toegenomen+of+afgenomen%3F+Deze+vraag+gaat+vooral+over+je+vertrouwen+in+de+maatschappij.&questions%5B2%5D%5Bbutton_pressed%5D=0&questions%5B2%5D%5Border%5D=4&questions%5B2%5D%5Bquestion_id%5D=6411&questions%5B2%5D%5Bexperiment_id%5D=540&questions%5B2%5D%5Bmodule_id%5D=2241&questions%5B2%5D%5Btrial_type%5D=button-response&questions%5B2%5D%5Btrial_index%5D=4&questions%5B2%5D%5Btime_elapsed%5D=13601&questions%5B2%5D%5Binternal_node_id%5D=0.0-4.0&X-CSRF-TOKEN=FXSLi3sPU8QY1jGkwPvZlOt4hTmvFsPlT08B0kIy"
data4 ="questions%5B0%5D%5Brt%5D=1813&questions%5B0%5D%5Bstimulus%5D=%3Cstrong%3EJe+wilt+iets+bestellen+en+je+kunt+een+onbekende+vragen+om+even+op+je+spullen+te+letten.+%3Cbr+%2F%3EWat+doe+je+na+het+vragen+en+tijdens+het+bestellen%3F%3C%2Fstrong%3E&questions%5B0%5D%5Bbutton_pressed%5D=0&questions%5B0%5D%5Border%5D=1&questions%5B0%5D%5Bquestion_id%5D=6429&questions%5B0%5D%5Bexperiment_id%5D=537&questions%5B0%5D%5Bmodule_id%5D=2249&questions%5B0%5D%5Btrial_type%5D=button-response&questions%5B0%5D%5Btrial_index%5D=2&questions%5B0%5D%5Btime_elapsed%5D=60054&questions%5B0%5D%5Binternal_node_id%5D=0.0-2.0&questions%5B1%5D%5Brt%5D=838&questions%5B1%5D%5Bstimulus%5D=In+hoeverre+voel+je+je+vrij+en+ontspannen+tijdens+dit+muziekfestival%3F+%3Cbr+%2F%3E%3Cstrong%3E+Hoeveel+vertrouwen+heb+in+de+ander%3F%3C%2Fstrong%3E&questions%5B1%5D%5Bbutton_pressed%5D=0&questions%5B1%5D%5Border%5D=2&questions%5B1%5D%5Bquestion_id%5D=6430&questions%5B1%5D%5Bexperiment_id%5D=537&questions%5B1%5D%5Bmodule_id%5D=2250&questions%5B1%5D%5Btrial_type%5D=button-response&questions%5B1%5D%5Btrial_index%5D=3&questions%5B1%5D%5Btime_elapsed%5D=60995&questions%5B1%5D%5Binternal_node_id%5D=0.0-3.0&questions%5B2%5D%5Brt%5D=1503&questions%5B2%5D%5Bstimulus%5D=%3Cstrong%3EHoe+voel+je+je+op+dit+moment%3F%3C%2Fstrong%3E%3Cbr+%2F%3E(Er+is+geen+goed+of+slecht+antwoord)&questions%5B2%5D%5Bbutton_pressed%5D=0&questions%5B2%5D%5Border%5D=3&questions%5B2%5D%5Bquestion_id%5D=6431&questions%5B2%5D%5Bexperiment_id%5D=537&questions%5B2%5D%5Bmodule_id%5D=2251&questions%5B2%5D%5Btrial_type%5D=button-response&questions%5B2%5D%5Btrial_index%5D=4&questions%5B2%5D%5Btime_elapsed%5D=62604&questions%5B2%5D%5Binternal_node_id%5D=0.0-4.0&X-CSRF-TOKEN=FXSLi3sPU8QY1jGkwPvZlOt4hTmvFsPlT08B0kIy"
data7 ="questions%5B0%5D%5Brt%5D=1356&questions%5B0%5D%5Bstimulus%5D=%3Cstrong%3EWat+is+voor+jou+de+meest+prettige+manier+om+wel+of+niet+aangesproken+te+worden%3F%3C%2Fstrong%3E&questions%5B0%5D%5Bbutton_pressed%5D=0&questions%5B0%5D%5Border%5D=1&questions%5B0%5D%5Bquestion_id%5D=6448&questions%5B0%5D%5Bexperiment_id%5D=534&questions%5B0%5D%5Bmodule_id%5D=2259&questions%5B0%5D%5Btrial_type%5D=button-response&questions%5B0%5D%5Btrial_index%5D=2&questions%5B0%5D%5Btime_elapsed%5D=6632&questions%5B0%5D%5Binternal_node_id%5D=0.0-2.0&questions%5B1%5D%5Brt%5D=1126&questions%5B1%5D%5Bstimulus%5D=%3Cstrong%3EOp+welke+afstand+vind+jij+het+nog+prettig+als+mensen+(heel)+dichtbij+je+komen%3F%3C%2Fstrong%3E&questions%5B1%5D%5Bbutton_pressed%5D=0&questions%5B1%5D%5Border%5D=2&questions%5B1%5D%5Bquestion_id%5D=6447&questions%5B1%5D%5Bexperiment_id%5D=534&questions%5B1%5D%5Bmodule_id%5D=2258&questions%5B1%5D%5Btrial_type%5D=button-response&questions%5B1%5D%5Btrial_index%5D=4&questions%5B1%5D%5Btime_elapsed%5D=9465&questions%5B1%5D%5Binternal_node_id%5D=0.0-4.0&questions%5B2%5D%5Brt%5D=1633&questions%5B2%5D%5Bstimulus%5D=%3Cstrong%3EHoe+zou+je+het+liefst+interactie+hebben+in+het+komende+uur+op+dit+festival%3F%3C%2Fstrong%3E+%3Cbr+%2F%3E(Er+is+geen+goed+of+slecht+antwoord)&questions%5B2%5D%5Bbutton_pressed%5D=0&questions%5B2%5D%5Border%5D=3&questions%5B2%5D%5Bquestion_id%5D=6449&questions%5B2%5D%5Bexperiment_id%5D=534&questions%5B2%5D%5Bmodule_id%5D=2260&questions%5B2%5D%5Btrial_type%5D=button-response&questions%5B2%5D%5Btrial_index%5D=5&questions%5B2%5D%5Btime_elapsed%5D=11204&questions%5B2%5D%5Binternal_node_id%5D=0.0-5.0&X-CSRF-TOKEN=FXSLi3sPU8QY1jGkwPvZlOt4hTmvFsPlT08B0kIy"

class TrustTrailUser(HttpUser):
    @task
    def trusttrail(self):
        # print(self.environment.parsed_options.customarg)

        # with self.client.get("trustrail/1", catch_response=True) as response:
        #     if response.text == "Gebruiker onbekend":
        #         response.failure("Sessie verlopen")
        #     elif response.elapsed.total_seconds() > 0.5:
        #         response.failure("Request took too long")

        # response = self.client.get("trusttrail/1")
        # print("Response text:", response.text)
        # #Welkom bij dit veldonderzoek 
        # if response.text != "Welkom":
        #     response.failure("Consent")
        # elif response.text != "Hoi, welkom":
        #     response.failure("Experiment")
        # elif response.elapsed.total_seconds() > 0.5:
        #     response.failure("Request took too long")

        if(self.environment.parsed_options.customarg == "gate"):
            response = self.client.request(
                "POST",
                "/webhooks/trustgate",
                headers = {'Content-Type': 'application/x-www-form-urlencoded'},
                data = {
                    "result": "666",
                    "total": "204",
                    # "score": random.randint(1,5),
                    "score": 5,
                    "remark": "locust"
                },
                catch_response=True,
            )
        else:
            data = data1
            if(self.environment.parsed_options.customarg == "data4"):
                data = data4
            if(self.environment.parsed_options.customarg == "data7"):
                data = data7

            response = self.client.request(
                "POST",
                "/results.json",
                headers = myheaders,
                data = data,
                catch_response=True,
            )

        # response = self.client.post("results.json", data=nameInquiry, headers=myheaders)
        print("Response status code:", response.status_code)
        print("Response text:", response.text)

        
