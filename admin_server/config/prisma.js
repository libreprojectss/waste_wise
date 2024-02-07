// config/database.js

/**
 * @typedef {import('prisma').PrismaClient} PrismaClient
 */

import PrismaClient from "@prisma/client";

/**
 * @returns {PrismaClient}
 */
const createPrismaClient = () => {
    const prisma = new PrismaClient();
    return prisma;
  };

export default createPrismaClient;
