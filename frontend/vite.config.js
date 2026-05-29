import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@locales': path.resolve(__dirname, '../locales')
    }
  },
  server: {
    port: 3000,
    open: true,
    allowedHosts: [
      'localhost',
      '127.0.0.1',
      'sb-1rp1ldc47qk6.vercel.run',
      '.vercel.run',
      '.vercel.app'
    ],
    proxy: {
      '/api': {
        target: 'http://localhost:5001',
        changeOrigin: true,
        secure: false
      }
    }
  }
})
