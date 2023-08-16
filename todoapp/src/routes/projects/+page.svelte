<script>
  import ProjectAPI from '$lib/api/project.js';
  import { onMount } from 'svelte';

  let projects = [];
  let newProject = {
    name: '',
  };

  async function getProjects() {
    try {
      projects = await ProjectAPI.get();
    } catch (error) {
      console.error(error);
    }
  }

  async function updateProject(project) {
    try {
      await ProjectAPI.update(project);
    } catch (error) {
      console.error(error);
    }
  }

  async function deleteProject(project) {
    try {
      await ProjectAPI.delete(project);
      projects = projects.filter((item) => item.id !== project.id);
    } catch (error) {
      console.error(error);
    }
  }

  async function addProject() {
    if (newProject.name.trim() === '') {
      return;
    }
    try {
      console.log(newProject);
      const res = await ProjectAPI.post(newProject);
      projects = [...projects, res];
      newProject = {
        name: '',
      };
    } catch (error) {
      console.error(error);
    }
  }

  onMount(getProjects);
</script>

<main>
  <h1>Projects:</h1>
  <ul>
    {#if projects.length > 0}
      {#each projects as project (project.id)}
        <li>
          <input
            type="text"
            bind:value={project.name}
            on:change={() => updateProject(project)}
          />
          <button on:click={() => deleteProject(project)}>x</button>
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
        bind:value={newProject.name}
      />
      <button on:click={() => addProject()}>+</button>
    </li>
  </ul>
</main>

<style></style>
