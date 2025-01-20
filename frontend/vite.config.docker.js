import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // Add this to expose to Docker network
    proxy: {
      '/sentiment-analysis': {
        target: 'http://backend:8000',  // Use service name in Docker
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets'
  }
})