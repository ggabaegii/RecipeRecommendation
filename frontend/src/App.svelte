<script>
    import { writable } from 'svelte/store';
    import Main from './pages/Main.svelte';
	
    //import Login from './Login.svelte';
    //import Signup from './Signup.svelte';
    // 다른 페이지 컴포넌트 import

    import { wrap } from 'svelte-spa-router/wrap';
	import Router from 'svelte-spa-router';

    // 라우터 설정
    const routes = {
        '/': wrap({ component: Main }),
        //'/login': wrap({ component: Login }),
        //'/signup': wrap({ component: Signup }),
        // 나머지 페이지 경로 추가
    };
</script>

<Router {routes} />