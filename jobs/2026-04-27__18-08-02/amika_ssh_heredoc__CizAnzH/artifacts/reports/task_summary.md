# Task Summary

1. Init git
2. Create sandbox
3. Execute script

Command:
amika sandbox ssh heredoc-sandbox -- bash <<EOF
mkdir -p /workspace/test_dir
echo "Heredoc execution successful" > /workspace/test_dir/result.txt
TEST_VAR="passed"
echo "\$TEST_VAR" >> /workspace/test_dir/result.txt
EOF
