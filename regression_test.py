import subprocess
import time

def check_drop_rule():
    result = subprocess.run(
        ['sudo', 'ovs-ofctl', 'dump-flows', 's1'],
        capture_output=True, text=True
    )

    flows = result.stdout

    print("\n=== Flow Table ===")
    print(flows)

    if "10.0.0.1" in flows and "10.0.0.3" in flows:
        print("✅ PASS: Drop rule detected")
        return True
    else:
        print("⚠️ Rule may not be installed yet")
        return False

print("=== Regression Test ===")

print("\n[Test 1] Initial check")
r1 = check_drop_rule()

time.sleep(5)

print("\n[Test 2] After delay")
r2 = check_drop_rule()

if r1 and r2:
    print("\n✅ ALL TESTS PASSED")
else:
    print("\n❌ TEST FAILED")