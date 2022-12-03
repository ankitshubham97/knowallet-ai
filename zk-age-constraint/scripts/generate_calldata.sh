cd /home/ubuntu/workspace/hawkeye/zk-age-constraint/
proof_file = rand -hex 20
public_file = rand -hex 20
echo $1 > proof_file
echo $2 > public_file
./node_modules/.bin/snarkjs zkey export soliditycalldata public_file proof_file
rm proof_file public_file