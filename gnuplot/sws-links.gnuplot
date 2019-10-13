set yrange [0:1]
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
set ylabel "Relative Amount of Resources" font ",20"

plot  'C:\Users\smallcat\Dropbox (個人)\eclipse\common_workspace\NEDO\sws.txt' using ($4)/($2):xtic(1) title "switch", 'C:\Users\smallcat\Dropbox (個人)\eclipse\common_workspace\NEDO\links.txt' using ($4)/($2) title "link"

#set terminal png         # gnuplot recommends setting terminal before output
#set output 'C:\Users\smallcat\Dropbox (個人)\eclipse\common_workspace\NEDO\sws-links.png'  

set term post eps color "GothicBBB-Medium-RKSJ-H, 20"  
#set term post eps color     
set output 'C:\Users\smallcat\Dropbox (個人)\eclipse\common_workspace\NEDO\sws-links.eps'  
replot
