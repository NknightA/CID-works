import styles from './index.module.sass';
import { useRouter } from 'next/router';

export default function Index() {
        return (
        <div className={styles.Container}>
            ログイン成功!!!
            <div>
                <a href='../'>戻る</a>
            </div>
        </div>
    )
}