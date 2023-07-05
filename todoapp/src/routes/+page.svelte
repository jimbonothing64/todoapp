<script>
    let tasks = ['Hi'];
    let newTask = '';
</script>
<main>
    <h1>Todos:</h1>
    {#if tasks.length > 0}
        <ul>
            <li>
                <input type="text">
                <input type="checkbox">
                <button>x</button>
            </li>
        </ul>
    {:else}
        <p>You have nothing to do :)</p>
    {/if}
</main>
<style></style>