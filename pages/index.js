import React, { useState } from 'react';
import { useRouter } from "next/router";
import styles from "./styles/home.module.sass";


export default function Home() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter();
    const auth = Number(router.query.auth);
    const AuthEnter = () =>{
        if(auth === 1){
            return <h1 style={{color: '#00ff00'}}>error!</h1> 
        }else if(auth === 2){
            return <h1 style={{color: '#ff0000'}}>Hacked your PC!!!</h1> 
        }else if(auth === 3){
            router.push("/hacked");
 
        }  
        else {}
    }

    const handleLogin = () => {
        // ユーザー名とパスワードを検証する処理をここに追加する
        // 例えば、ユーザー名が "example" で、パスワードが "password" の場合にログインが成功したとする
        if (password === "1986") {
            // ログインが成功した場合は、ユーザーページに遷移する
            router.push("/succes");
        } else {
            return router.push("/?auth=1");
        } 
    };
    return (
        <div className={styles.Container}>
            <div className={styles.header}>
                <h1>CID 総当たり攻撃テスト</h1>
            </div>
            <div className={styles.ContainerInner}>
                <div className={styles.Main}>
                    <div>
                        <input
                            className={styles.Input}
                            type="password"
                            placeholder="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <br />
                        <div className={styles.buttoncontainer}>
                            <button onClick={handleLogin} className={styles.button}>ログイン</button>
                        </div>
                        <AuthEnter/>
                        <a href='/touroku'>新規登録</a>
                    </div>
                </div>
            </div>
        </div>
    );
}

console.log("uername is 11111");
console.log("password is 11111");