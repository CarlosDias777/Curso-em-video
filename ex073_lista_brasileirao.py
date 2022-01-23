#tabela de 19 de janeiro de 2022
times = ('Atletico-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense',
'America-MG','Atletico-GO','Santos','Ceará','Internacional','São Paulo','Athleticp-PR','Cuiabá',
'Juventude','GRÊMIO','Bahia','Sport','Chapecoence')

print(f"""Tabela de 19 de janeiro de 2022 do Brasileirão!
Os primeiros 5 colocados são {times[:5]}!
Os ultimos 4 colocados são {times[15:]}
Os time em ordem alfabetica {sorted(times)}
A chapecoence está em {times.index('Chapecoence')+1}° lugar""")