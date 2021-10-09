###
 # @Author: fghpdf
 # @Date: 2021-10-09 12:05:55
 # @LastEditTime: 2021-10-09 12:19:50
 # @LastEditors: fghpdf
### 

RED='\033[0;31m'
NC='\033[0m' # No Color

problem_name=$1;
problem_length=echo ${problem_name} | wc -l;

if [[ ${problem_length} -le 0 ]]; then
  echo "${RED} must input problem name ${NC} \n";
fi

