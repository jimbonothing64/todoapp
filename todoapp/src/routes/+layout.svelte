<script>
  import '../app.postcss';
  import { page } from '$app/stores';

  import { Navbar, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
</script>

<Navbar
  let:hidden
  let:toggle
>
  <NavHamburger on:click={toggle} />
  <NavUl {hidden}>
    <NavLi
      href="/"
      active={$page.url.pathname === '/'}>Todo</NavLi
    >
    <NavLi
      href="/projects"
      active={$page.url.pathname === '/projects'}>Projects</NavLi
    >
    <NavLi
      href="/tasks"
      active={$page.url.pathname === '/tasks'}>Tasks</NavLi
    >
  </NavUl>
</Navbar>
<slot />
