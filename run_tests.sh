#!/bin/bash

echo "=== 清理上次报告 ==="
rm -rf ./allure-results
rm -rf ./allure-report

echo "=== 运行测试 ==="
pytest tests/ \
  --alluredir=./allure-results \
  --clean-alluredir \
  -v

echo "=== 生成报告 ==="
allure generate ./allure-results -o ./allure-report --clean

echo "=== 打开报告 ==="
allure open ./allure-report