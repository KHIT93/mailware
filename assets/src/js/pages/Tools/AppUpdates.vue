<template>
<mg-page>
  <div class="sm:container mx-auto sm:px-4 pt-6 pb-8">
        <div class="card p-2">
            <div v-if="!user.is_staff">
                <p>You are not authorized to view this page</p>
            </div>
            <div v-else>
                <template v-if="updates_loading">
                    <div class="text-center">
                        <h1 class="text-2xl mb-2 text-center border-b pb-1">Checking for updates</h1>
                        <svg class="w-16 h-16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                            <circle cx="50" cy="50" fill="none" stroke-linecap="round" r="40" stroke-width="4" stroke="#000" stroke-dasharray="62.83185307179586 62.83185307179586" transform="rotate(66 50 50)">
                                <animateTransform attributeName="transform" type="rotate" calcMode="linear" values="0 50 50;360 50 50" keyTimes="0;1" dur="1s" begin="0s" repeatCount="indefinite"></animateTransform>
                            </circle>
                        </svg>
                        <p class="text-center">Please wait...</p>
                    </div>
                </template>
                <template v-else>
                    <div class="table-wrapper">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Release</th>
                                    <th>Release Date</th>
                                    <th>Release Notes</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-if="releases == 0">
                                    <td colspan="3">No new releases are available</td>
                                </tr>
                                <tr v-for="release in releases" :key="release.id" v-else>
                                    <td>{{release.name}}</td>
                                    <td>{{release.created_at | ago }}</td>
                                    <td>
                                        <a :href="release.html_url">See release notes</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="flex items-center w-full">
                            <button @click="getReleases" type="button" class="bg-blue-500 hover:bg-blue-600 no-underline text-white font-semibold py-2 px-4 border border-blue-500 hover:border-bleu-600 text-sm rounded">Check for updates</button>
                        </div>
                    </div>
                </template>
            </div>
        </div>
  </div>
</mg-page>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';
export default {
    data: () => {
        return {
            updates_loading: false,
            releases: []
        }
    },
    mounted() {
        if (this.user.is_staff) {
            
        }
        this.setLoading(false);
    },
    computed: {
        ...mapGetters(['isLoggedIn', 'user', 'loading', 'app_info'])
    },
    methods: {
        getReleases() {
            this.updates_loading = true;
            axios.get('https://api.github.com/repos/khit93/mailguardian/releases').then(response => {
                let all = response.data;
                let current = all.filter(release => {
                    return release.name == this.app_info.app_version;
                })[0];
                // this.releases = all;
                this.releases = all.filter(release => {
                    return release.published_at > current.published_at;
                })
                this.updates_loading = false;
            }).catch(error => {
                this.updates_loading = false;
            });
        },
        ...mapMutations(['setLoading'])
    }
}
</script>