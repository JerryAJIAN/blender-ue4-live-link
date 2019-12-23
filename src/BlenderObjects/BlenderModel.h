/* This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program. If not, see <http://www.gnu.org/licenses/>.
*/
#pragma once

class BlenderModel
{
public:
    BlenderModel(char* NewLongName);
    int32 Add(int32 x, int32 y);
    int32 Sub(int32 x, int32 y);
    char* Name;
    char* LongName;
    TArray<BlenderModel*> Children;
};
