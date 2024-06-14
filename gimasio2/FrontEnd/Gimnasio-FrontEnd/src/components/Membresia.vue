<template>
    <h1 class="mb-4 text-2xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-4xl dark:text-black">
        Membresías</h1>
    <hr>
    <br>
    <form>
        <input
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5 col-span-2"
            type="text" placeholder="Nombre Membresia"
        />
        
        <select id="countries" class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5">
            <option selected>Tipo</option>
            <option value="M">Basica</option>
            <option value="F">Media</option>
            <option value="NB">Premium</option>
        </select>
        
        <input
            class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
            type="number" placeholder="Precio"
        />
    
        
        <a href="/" class="col-span-2" >
            <button
                class="mt-5 tracking-wide font-semibold bg-blue-700 text-gray-100 w-full py-4 rounded-lg hover:bg-red-900 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none col-span-2">
                <svg class="w-6 h-6 -ml-2" fill="none" stroke="currentColor" stroke-width="2"
                    stroke-linecap="round" stroke-linejoin="round">
                    <path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
                    <circle cx="8.5" cy="7" r="4" />
                    <path d="M20 8v6M23 11h-6" />
                </svg>
                <span class="ml-3 uppercase">
                    Registrar
                </span>
            </button>
        </a>
    </form>

    <div>
        <Tmembresia/>
    </div>
    
</template>

<script>
    import Tmembresia from './tmembresias.vue'
        export default{
            components:{
                Tmembresia
            }
        }
</script>