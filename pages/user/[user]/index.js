import styles from './index.module.sass';
import { useRouter } from 'next/router';

export default function Index() {
    const router = useRouter();
    const auth = Number(router.query.auth);
    const Autherror = () => {
        if ( auth === 1 ) {
        } else {
            router.push('../../');
        }
    }
    return (
        <div className={styles.Container}>
            ログイン成功!!!
            <div>
                <a href='../'>戻る</a>
                <Autherror />
            </div>
        </div>
    )
}