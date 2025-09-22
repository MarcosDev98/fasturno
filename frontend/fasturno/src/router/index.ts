import { createRouter, createWebHistory } from 'vue-router'
import RegistrarUsuario from "../pages/RegistrarUsuario.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/registro',
      name: "registro",
      component: RegistrarUsuario
    }
  ],
})

export default router
