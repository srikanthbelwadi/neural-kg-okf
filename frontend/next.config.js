/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${process.env.BACKEND_API_URL || 'http://127.0.0.1:8099'}/:path*`,
      },
      {
        source: '/ask',
        destination: `${process.env.BACKEND_API_URL || 'http://127.0.0.1:8099'}/ask`,
      },
      {
        source: '/healthz',
        destination: `${process.env.BACKEND_API_URL || 'http://127.0.0.1:8099'}/healthz`,
      },
      {
        source: '/sources',
        destination: `${process.env.BACKEND_API_URL || 'http://127.0.0.1:8099'}/sources`,
      }
    ];
  },
};

module.exports = nextConfig;
