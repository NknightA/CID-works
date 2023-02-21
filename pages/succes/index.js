import styles from './index.module.sass';
import { useRouter } from 'next/router';

export default function Index() {
    return (
        <div>
            <div className={styles.Container}>
                ログイン成功!!!
                <div>
                    <a href='../'>戻る</a>
                </div>
            </div>
            <div className={styles.Container_under}>
                <div>
                    <p>Your PhoneNumber 222-22222-22222 ?</p>
                    <p>Your Credit Card 1222-2322-3422 ?</p>
                </div>
            </div>
        </div>
    )
}