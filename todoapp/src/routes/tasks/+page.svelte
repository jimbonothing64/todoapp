<script>
  import axios from 'axios';
  import { onMount } from 'svelte';

  let tasks = [];
  let newTask = {
    text: '',
    completed: false,
  };

  async function getTasks() {
    try {
      const response = await axios.get('http://localhost:8000/tasks/');
      tasks = response.data;
    } catch (error) {
      console.error(error);
    }
  }

  async function updateTask(task) {
    try {
      await axios.put(`http://localhost:8000/tasks/${task.id}/`, task);
    } catch (error) {
      console.error(error);
    }
  }

  async function deleteTask(task) {
    try {
      await axios.delete(`http://localhost:8000/tasks/${task.id}/`, task);
      tasks = tasks.filter((item) => item.id !== task.id);
    } catch (error) {
      console.error(error);
    }
  }

  async function addTask() {
    if (newTask.text.trim() === '') {
      return;
    }
    try {
      const res = await axios.post('http://localhost:8000/tasks/', newTask);
      tasks = [...tasks, res.data];
      newTask = {
        text: '',
        completed: false,
      };
    } catch (error) {
      console.error(error);
    }
  }

  onMount(getTasks);
</script>

<main>
  <h1>Todos:</h1>
  <ul>
    {#if tasks.length > 0}
      {#each tasks as task (task.id)}
        <li>
          <input
            type="text"
            bind:value={task.text}
            on:change={() => updateTask(task)}
          />
          <input
            type="checkbox"
            bind:checked={task.completed}
            on:change={() => updateTask(task)}
          />
          <button on:click={() => deleteTask(task)}>x</button>
        </li>
      {/each}
    {:else}
      <li>
        <p>You have nothing to do :)</p>
      </li>
    {/if}
    <li>
      <input
        type="text"
        bind:value={newTask.text}
      />
      <input
        type="checkbox"
        bind:value={newTask.completed}
      />
      <button on:click={() => addTask()}>+</button>
    </li>
  </ul>
</main>

<style></style>
