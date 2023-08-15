<script>
    import axios from 'axios';
    import { onMount } from 'svelte';
    
    axios.defaults.baseURL = "http://localhost:8000/projects/";

    let projects = [];
    let newProject = {
        name: "",
    };

    async function getProjects() {
        try {
            const response = await axios.get();
            projects = response.data;
        } catch (error) {
        console.error(error);
        }
    }

    async function updateProject(project) {
        try {
            await axios.put(`http://localhost:8000/projects/${project.id}/`, project);
        } catch (error) {
            console.error(error);
        }
    }

    async function deleteProject(project) {
        try {
            await axios.delete(`http://localhost:8000/projects/${project.id}/`, project);
            projects = projects.filter(item => item.id !== project.id);
        } catch (error) {
            console.error(error);
        }
    }

    async function addProject() {
        if (newProject.text.trim() === "") {
            return
        }
        try {
            const res = await axios.post('http://localhost:8000/projects/', newproject);
            projects = [...projects, res.data];
            newProject = {
                name: "",
            };
        }  catch (error) {
            console.error(error);
        }
        
    }

    onMount(getProjects);
</script>
<main>
    <h1>Projects:</h1>
    <ul>
    {#if projects.length > 0}
        {#each projects as project (project.id) }
            <li>
                <input type="text" bind:value={project.name} on:change={() => updateProject(project)}>
                <button on:click={() => deleteProject(project)}>x</button>
            </li>
        {/each}
    {:else}
    <li>
        <p>You have nothing to do :)</p>
    </li>
    {/if}
    <li>
        <input type="text" bind:value={newProject.text}>
        <button on:click={()=> addProject()}>+</button>
    </li>
    </ul>
</main>
<style></style>