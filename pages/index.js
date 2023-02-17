import React,{useState} from 'react';
import {useRouter} from "next/router";
import styles from "../styles/home.module.sass";


function LoginPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter();

    const handleLogin = () => {
        // ユーザー名とパスワードを検証する処理をここに追加する
        // 例えば、ユーザー名が "example" で、パスワードが "password" の場合にログインが成功したとする

        if (username === "111111" && password === "111111") {
            // ログインが成功した場合は、ユーザーページに遷移する
            router.push("/user/[user]/", `/user/${username}/`);
        } else {
            router.push("/error");

        }
    };

    return (
        <div className={styles.Main}>
            <div>
                <input
                    className={styles.Input}
                    type="text"
                    placeholder="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    
                /></div>
            <div>
                <input
                    className={styles.Input}
                    type="password"
                    placeholder="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br/>
                <div className={styles.buttoncontainer}>
                    <button onClick={handleLogin} className={styles.button}>ログイン</button>
                </div>
            </div>
        </div>
    );
}

export default function Home() {
    return (
        <div className={styles.Container}>
            <div className={styles.header}>
                <h1>CID 総当たり攻撃テスト</h1>
            </div>
            <div className={styles.ContainerInner}>
                <LoginPage/>
            </div>
            
        </div>
    );
}

console.log("uername is 11111");
console.log("password is 11111");