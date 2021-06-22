#! /usr/bin/env sh
echo "##########################"
echo "### Running e2e tests! ###"
echo "##########################\n"
count=0 # number of test cases run so far

for folder in `ls -d tests_e2e/*/ | sort -V`; do
    name=$(basename $folder)
    
    echo Running test $name.

    config_file=tests_e2e/$name/$name.config
    expected_file=tests_e2e/$name/$name.out
    in_file=tests_e2e/$name/$name.in

    if (($count != 13)); then
        python3 run.py $config_file < $in_file | diff - $expected_file || echo "Test $name: failed!\n"
    else
        python3 run.py "file_does_not_exist.txt" | diff - $expected_file || echo "Test $name: failed!\n"
    fi

    count=$((count+1)) 
    
done

echo "Finished running $count tests!"