<template>
    <div class="text-center text-gray-700 py-6">
        <div>
            <div class="mb-2">
                <span class="text-5xl">Page not found</span>
            </div>
            <div class="uppercase">
                Whoops! The page you were looking for does not seem to exist.
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        mounted() {
            console.log('Page not found.');
            this.$store.commit('setLoading', false);
        }
    }
</script>