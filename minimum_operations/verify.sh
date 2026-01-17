#!/bin/bash

echo "======================================"
echo "MINIMUM OPERATIONS PROJECT VERIFICATION"
echo "======================================"
echo ""

# Check file exists
echo "1. Checking files..."
[ -f "0-minoperations.py" ] && echo "   ✅ 0-minoperations.py exists" || echo "   ❌ Missing 0-minoperations.py"
[ -f "README.md" ] && echo "   ✅ README.md exists" || echo "   ❌ Missing README.md"

# Check shebang
echo ""
echo "2. Checking shebang..."
head -1 0-minoperations.py | grep -q "#!/usr/bin/python3" && echo "   ✅ Correct shebang" || echo "   ❌ Wrong shebang"

# Check executable
echo ""
echo "3. Checking executable permission..."
[ -x "0-minoperations.py" ] && echo "   ✅ File is executable" || echo "   ❌ File not executable"

# Check PEP8
echo ""
echo "4. Checking PEP8 compliance..."
pycodestyle 0-minoperations.py 2>/dev/null
if [ $? -eq 0 ]; then
    echo "   ✅ PEP8 compliant"
else
    echo "   ❌ PEP8 issues found"
fi

# Test functionality
echo ""
echo "5. Testing functionality..."
./0-main.py > /tmp/minops_output.txt 2>&1
if grep -q "Min # of operations to reach 4 char: 4" /tmp/minops_output.txt && \
   grep -q "Min # of operations to reach 12 char: 7" /tmp/minops_output.txt; then
    echo "   ✅ Tests pass"
else
    echo "   ❌ Tests fail"
fi

# Check documentation
echo ""
echo "6. Checking documentation..."
python3 -c 'import sys; sys.exit(0 if __import__("0-minoperations").__doc__ else 1)' && \
    echo "   ✅ Module documented" || echo "   ❌ Module not documented"

python3 -c 'import sys; sys.exit(0 if __import__("0-minoperations").minOperations.__doc__ else 1)' && \
    echo "   ✅ Function documented" || echo "   ❌ Function not documented"

echo ""
echo "======================================"
echo "Verification complete!"
echo "======================================"
