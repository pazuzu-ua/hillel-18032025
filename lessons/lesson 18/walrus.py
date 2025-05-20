info = { 
    'name': 'Sam' 
}

# if info.get('name'):
#     name = info.get('name')
#     print(f"Hello, {name}")

# -------- WALRUS OPERATOR ---- МОРЖОВИЙ ОПЕРАТОР ---->               :=
# if name := info.get('name'):
#     print(f"Hello, {name}")

data = {
    'likes_dogs': False
}
if ( value := data.get('likes_dogs') ) is not None:
    print(f'Likes dogs: {value}')
