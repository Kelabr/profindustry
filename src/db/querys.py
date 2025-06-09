import bcrypt

def createUsers(coon, name, email, phone, password, sex):

    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        with coon.cursor() as cur:
            cur.execute('INSERT INTO users (name, email, phone, password, sex) VALUES (%s, %s, %s, %s, %s)', (name, email, phone, password_hash, sex))
            coon.commit()

            return True
    
    except Exception as e:
        print(f'Erro: {e}')
        coon.rollback()

        return None


def deleteUser(coon, email):
    try:
        with coon.cursor() as cur:
            cur.execute('DELETE FROM users WHERE email=%s', (email,))
            coon.commit()

            return True
        
    except Exception as e:
        print(f'Erro: {e}')
        coon.rollback()

        return None


def updateUser(coon, data:dict):
    try:
        with coon.cursor() as cur:

            cur.execute('SELECT id FROM users WHERE email=%s', (data['email'], ))
            result = cur.fetchone()

            if not result:
                print('Usuário não encontrado')
                return None
            
            iduser = result[0]


            password_hash = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')



            cur.execute('UPDATE users SET name = COALESCE(%s, name), email = COALESCE(%s, email), phone = COALESCE(%s, phone), password = COALESCE(%s, password), sex = COALESCE(%s, sex) WHERE id=%s', (data['name'], data['email'], data['phone'], password_hash, data['sex'], iduser))
            coon.commit()
            return True
        
    except Exception as e:
        print(f'Erro: {e}')
        coon.rollback()

        return None


def loginUser(coon, email, password):
    try:
        with coon.cursor() as cur:

            cur.execute('SELECT * FROM users WHERE email=%s', (email,))
            result = cur.fetchone()

            if not result:
                print('Usuário não encontrado')
                return None
            
            comppassword = bcrypt.checkpw(password.encode(), result[4].encode())

            if not comppassword:
                print('Senha incorreta')
                return None
            
            return {'name':result[1], 'email':result[2]}
        
    except Exception as e:
        print(f'Erro: {e}')
        return None
            

    

    
