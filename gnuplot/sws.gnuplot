set yrange [0:1200]
set key top left font "GothicBBB-Medium-RKSJ-H, 16"
#set key c tm horizontal box font "GothicBBB-Medium-RKSJ-H, 13"
set grid
set style data histograms
#set style fill solid 1.00 border -1
set style fill pattern 3 border -1
#set title "Average Queuing Time (16 nodes per cabinet)"
#set xtics rotate by -5 font "GothicBBB-Medium-RKSJ-H, 20"
set xtics font "GothicBBB-Medium-RKSJ-H, 20"
set xlabel "Network Size" font "GothicBBB-Medium-RKSJ-H, 20"
set ylabel "Number of Switches" font ",20"

plot  'C:\Users\smallcat\Dropbox (å¬êl)\eclipse\common_workspace\NEDO\sws.txt' using ($2):xtic(1) title "2-D mesh", '' using ($3) title "2-D torus", '' using ($4) title "generator"

#set terminal png         # gnuplot recommends setting terminal before output
#set output 'C:\Users\smallcat\Dropbox (å¬êl)\eclipse\common_workspace\NEDO\sws.png'  

set term post eps color "GothicBBB-Medium-RKSJ-H, 20"  
#set term post eps color     
set output 'C:\Users\smallcat\Dropbox (å¬êl)\eclipse\common_workspace\NEDO\sws.eps'  
replot
