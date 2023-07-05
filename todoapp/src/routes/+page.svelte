<script>
    import axios from 'axios';
    import { onMount } from 'svelte';
    let tasks = [];
    let newTask = '';

    async function getTasks() {
        try {
        const response = await axios.get('http://localhost:8000/tasks/');
        tasks = response.data;
        } catch (error) {
        console.error(error);
        }
    }
    onMount(getTasks);
</script>
<main>
    <h1>Todos:</h1>
    {#if tasks.length > 0}
        <ul>
            {#each tasks as task (task.id) }
                <li>
                    <input type="text" bind:value={task.text}>
                    <input type="checkbox" bind:checked={task.completed}>
                    <button>x</button>
                </li>
            {/each}
            <li>
                <input type="text">
                <input type="checkbox">
                <button>+</button>
            </li>
        </ul>
    {:else}
        <p>You have nothing to do :)</p>
    {/if}

</main>
<style></style>