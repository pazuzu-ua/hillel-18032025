# -- 1. raw password (HTTP)


# -- 2. HTTPS
# 0_0 ->  "gfhhRFGFhtrh56456"  ->  [S]
# BD => { pasword => "password" }

# -- 3. Hashing - хешування
# шифрування в один кінець
# "password" => f() => "cvgfefdgfgr"
# 1. я завжди отримаю ті самі дані
# 2. я не можу отримати дані назад
# 3. колізії мінімальні
# 4. вихідні дані завжди однієї довжини

# 0_0 -> "password" -> [S] -> f() -> "VVVVVVV" -> [BD]
# 0_0 -> "password" -> [S] -> f() -> "VVVVVVV"     ( == )    <- "VVVVVVV"

# rainbow tables

# -- 4. salt / pepper
# 0_0 -> "password" ->  [S]:
#                1. generate salt ("fgdfhgrgdg")
#                2. password + salt -> hash
#                3. hash + salt
# pepper - він однаковий для всіх, але зберігається в коді

# -- argon2 (спеціально сповільнені алгоритми)

# -- двофакторна авторизація / зміна пароля



# -------------------------------
# pip install argon2_cffi
from argon2 import PasswordHasher


ph = PasswordHasher()
hashed = ph.hash( "12345678" )

try:
    ph.verify( hashed, "1245678" )
    print("ALL IS GOOD")
except:
    print("WRONG PASSWORD")
