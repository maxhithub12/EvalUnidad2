import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/LoginView.vue'
import RegisterUser from '@/components/RegisterUser.vue'
import  Home from '@/components/Home.vue'
import Menu from '@/components/Menu.vue'
import Persona from '@/components/Persona.vue'
import Base from '@/components/Base.vue'
import Membresia from '@/components/Membresia.vue'
import Miembro from '@/components/Miembro.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: RegisterUser
    },
   
    {
      path: '/home',
      name: 'home',
      component: Menu,
      children:[
        {path:'/base', name: 'base', component:Base},
        {path:'/persona', name: 'persona', component:Persona},
        {path:'/membresia', name: 'membresia', component:Membresia},
        {path:'/miembro', name: 'miembro', component:Miembro}
      ]
    }
  ]
})

export default router
