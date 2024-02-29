import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";
import path from "path";
import { generate_priority_queue } from "./grpc/services/getClusterPriorityQueue.js";

import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const CLUSTER_PROTO_PATH = path.resolve(__dirname, 'grpc/protos/cluster.proto');
console.log(CLUSTER_PROTO_PATH);

const packageDefinition = protoLoader.loadSync(CLUSTER_PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
});

const cluster_proto = grpc.loadPackageDefinition(packageDefinition);
console.log(cluster_proto);

function main() {
    const server = new grpc.Server();
    server.addService(cluster_proto.ClusterService.service, {
        GeneratePriorityQueue: generate_priority_queue
    });
    server.bindAsync('127.0.0.1:50051', grpc.ServerCredentials.createInsecure(),() => {
        server.start();
      });
    console.log('Server running at http://127.0.0.1:50051');
}

main();