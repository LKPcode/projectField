<template>
    <div>
        <Header />
        <HomeSearch />
        <ProfileInfo />
        <Field />
        <Footer />

    </div>
</template>

<script>

import Header from '@/components/Header.vue'
import HomeSearch from '@/components/home/HomeSearch.vue'
import Footer from '@/components/Footer.vue'
import ProfileInfo from '@/components/profile/ProfileInfo.vue'
import Field from '@/components/profile/Field.vue'

export default {
    name: 'Profile',
    components: {
        Header,
        HomeSearch,
        Footer,
        ProfileInfo,
        Field
  }
}
</script>

<style scoped>

</style>