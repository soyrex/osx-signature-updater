<?php
$names = array(
	'alex'=>'Alex Holt',
	'bob'=>'Bob Smith',
);
$name = strtolower($_REQUEST['name']);
$fullname = $names[$name];
?>
Content-Transfer-Encoding: 7bit 
Content-Type: text/html; charset=us-ascii 

<body style="">
<hr style="height: 1px; border:none; border-top: 1px solid #ccc;margin-top: 20px;margin-bottom:20px;" />
<table border="0" cellpadding="0" cellspacing="0" style="font-family: Helvetica, Arial, sans-serif">
<tbody>
<tr>
<td valign="top" style="padding-right: 10px; padding-top: 5px;">
<img src="http://holtseafood.com/img/elogo.png" />
</td>
<td valign="top" nowrap="">
<b>
<big><?php echo $fullname?></big>
</b>
<div>
<small>
<b>HOLT SEAFOOD COMPANY</b>
</small>
</div>
<div>
	<span style="display: block;float:left;margin-right: 10px;">w <a style="color:#DD0000" href="http://holtseafood.com/email/"><b>holtseafood.com</b></a></span> 
	<span style="display: block;float:left;">p <a style="color:#DD0000" href="tel:123456789"><b>+61 (2) 1234 1234</b></a></span>
</div>
</td>
</tr>
<?php /*<tr>
	<td>&nbsp;</td>
	<td>&nbsp;</td>
	<td><p>&nbsp;<br><strong style="color: #666">2017-18 Holidays!!</strong> <strong style="color:#a00">Our offices will close on Thursday 21 December 2017 and re-open on Monday&nbsp;8&nbsp;January&nbsp;2018.</strong></p>
	</td>
</tr> */ ?>
</tbody>
</table>
</body>
<!-- <?=time()?> -->