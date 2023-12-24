<?xml version="1.0" encoding="utf-8"?>
<!--https://magictool.ai/tool/xslt-transformation/-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" indent="yes"/>

	<xsl:template match="/">
		<html>
			<head>
				<style>
					body {
						font-family: Arial;
					}
				</style>
			</head>
			<body>
				<h1>
					<xsl:text>Timetable&#xa;</xsl:text>
				</h1>

				<table>
					<tr>
						<th>Day</th>
						<th>Time</th>
						<th>Title</th>
						<th>Teacher</th>
						<th>Type</th>
						<th>Room</th>
					</tr>

					<xsl:for-each select="timetable/day">
						<xsl:for-each select="./class">
							<tr>
								<!--<td rowspan="{count(../class)}">-->
								<td>
									<xsl:value-of select="../@name"/>
								</td>
								<td>
									<xsl:value-of select="@startTime"/>-<xsl:value-of select="@endTime"/>
								</td>
								<td>
									<xsl:value-of select="title"/>
								</td>
								<td>
									<xsl:value-of select="teacher"/>
								</td>
								<td>
									<xsl:value-of select="@type"/>
								</td>
								<td>
									<xsl:value-of select="room/roomNumber"/><xsl:text>[</xsl:text><xsl:value-of select="room/buildingNumber"/><xsl:text>]</xsl:text>
								</td>
							</tr>
						</xsl:for-each>	
					</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>

</xsl:stylesheet>
