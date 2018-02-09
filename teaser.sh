num_item=5
num_epoch=19
for (( item=1; item<=$num_item; item++ ))
do
	echo "Item $item"
	for var in {1..$num_epoch}
	for (( var=1; var<=$num_epoch; var++ ))
	do 
		convert ./saved/x_$var-$item.binvox.png \
			./saved/t_$var-$item.binvox.png \
			./saved/g_$var-$item.binvox.png \
			+append -transparent white \
			./saved/merged_$var-$item.png
	done
done
