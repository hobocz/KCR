import { createRouter, createWebHistory } from "vue-router"

const Dashboard = () => import("./views/Dashboard.vue")
const PlayerBatting = () => import("./components/PlayerBatting.vue")
const PlayerPitching = () => import("./components/TopYoungPitchersChart.vue")

const routes = [
    { path: "/", name: "home", component: Dashboard },
    { path: "/dashboard", name: "dashboard", component: Dashboard },
    { path: "/batting", name: "batting", component: PlayerBatting },
    { path: "/pitching", name: "pitching", component: PlayerPitching },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
