import React,{useState} from 'react';
import {useRouter} from "next/router";

function LoginPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter();

    const handleLogin = () => {
        // ユーザー名とパスワードを検証する処理をここに追加する
        // 例えば、ユーザー名が "example" で、パスワードが "password" の場合にログインが成功したとする

        if (username === "11111" && password === "11111") {
            // ログインが成功した場合は、ユーザーページに遷移する
            router.push("/user/[user]/", `/user/${username}/`);
        }
    };

    return (
        <div>
            <h1>CID debug</h1>
            <div>
                <input
                    type="text"
                    placeholder="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    
                /></div>
            <div>
                <input
                    type="password"
                    placeholder="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br/>
                <button onClick={handleLogin}>ログイン</button>
            </div>
        </div>
    );
}

export default function Home() {
    return (
        <div >
            <div >
                <LoginPage/>
            </div>
        </div>
    );
}

console.log("uername is 11111");
console.log("password is 11111");